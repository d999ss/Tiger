#!/usr/bin/env python3
"""
Visual Regression Comparison Tool
Compare screenshots from different runs to detect visual changes
"""

import os
import json
from pathlib import Path
from datetime import datetime
import sys

try:
    from PIL import Image, ImageChops, ImageStat
    PILLOW_AVAILABLE = True
except ImportError:
    PILLOW_AVAILABLE = False
    print("⚠️  Pillow not installed. Install with: pip install Pillow")
    print("   Running in basic mode (file comparison only)\n")


class ScreenshotComparator:
    def __init__(self, base_path="/Users/donnysmith/Desktop/Tiger CMS/qa-automation"):
        self.base_path = Path(base_path)
        self.screenshots_dir = self.base_path / "screenshots"
        
    def list_runs(self):
        """List all available screenshot runs"""
        if not self.screenshots_dir.exists():
            print("❌ No screenshots directory found")
            return []
            
        runs = []
        for item in sorted(self.screenshots_dir.iterdir(), reverse=True):
            if item.is_dir():
                results_file = item / "results.json"
                if results_file.exists():
                    with open(results_file) as f:
                        data = json.load(f)
                    runs.append({
                        "timestamp": item.name,
                        "path": item,
                        "count": len(data)
                    })
        return runs
        
    def compare_images(self, img1_path, img2_path):
        """Compare two images and return difference percentage"""
        if not PILLOW_AVAILABLE:
            return None
            
        try:
            img1 = Image.open(img1_path)
            img2 = Image.open(img2_path)
            
            # Ensure same size
            if img1.size != img2.size:
                img2 = img2.resize(img1.size)
                
            # Calculate difference
            diff = ImageChops.difference(img1, img2)
            stat = ImageStat.Stat(diff)
            
            # Calculate average difference across all channels
            avg_diff = sum(stat.mean) / len(stat.mean)
            max_value = 255.0
            diff_percent = (avg_diff / max_value) * 100
            
            return diff_percent
            
        except Exception as e:
            print(f"❌ Error comparing images: {e}")
            return None
            
    def compare_runs(self, run1_timestamp, run2_timestamp):
        """Compare two screenshot runs"""
        run1_dir = self.screenshots_dir / run1_timestamp
        run2_dir = self.screenshots_dir / run2_timestamp
        
        if not run1_dir.exists() or not run2_dir.exists():
            print("❌ One or both runs not found")
            return
            
        print(f"📊 Comparing:")
        print(f"   Baseline: {run1_timestamp}")
        print(f"   Current:  {run2_timestamp}\n")
        
        # Load results
        with open(run1_dir / "results.json") as f:
            run1_data = {item['name']: item for item in json.load(f)}
            
        with open(run2_dir / "results.json") as f:
            run2_data = {item['name']: item for item in json.load(f)}
            
        # Compare each site
        results = []
        
        for site_name in run1_data:
            if site_name not in run2_data:
                print(f"⚠️  {site_name}: Missing in current run")
                continue
                
            site1 = run1_data[site_name]
            site2 = run2_data[site_name]
            
            if site1['status'] != 'success' or site2['status'] != 'success':
                print(f"⚠️  {site_name}: Error in one or both runs")
                continue
                
            img1_path = site1['screenshot']
            img2_path = site2['screenshot']
            
            # Check if files exist
            if not Path(img1_path).exists() or not Path(img2_path).exists():
                print(f"⚠️  {site_name}: Screenshot file(s) missing")
                continue
                
            if PILLOW_AVAILABLE:
                diff_percent = self.compare_images(img1_path, img2_path)
                
                if diff_percent is not None:
                    status = "🔴 CHANGED" if diff_percent > 5 else "✅ SAME"
                    print(f"{status} {site_name}: {diff_percent:.2f}% difference")
                    
                    results.append({
                        "site": site_name,
                        "difference": diff_percent,
                        "changed": diff_percent > 5
                    })
            else:
                # Basic file size comparison
                size1 = Path(img1_path).stat().st_size
                size2 = Path(img2_path).stat().st_size
                size_diff = abs(size1 - size2) / size1 * 100
                
                status = "🔴 CHANGED" if size_diff > 10 else "✅ LIKELY SAME"
                print(f"{status} {site_name}: {size_diff:.1f}% size difference")
                
        # Generate summary report
        if PILLOW_AVAILABLE and results:
            changed_count = sum(1 for r in results if r['changed'])
            unchanged_count = len(results) - changed_count
            
            print(f"\n📈 Summary:")
            print(f"   Changed: {changed_count}")
            print(f"   Unchanged: {unchanged_count}")
            print(f"   Total: {len(results)}")
            
            # Save comparison report
            report_path = self.screenshots_dir / f"comparison_{run1_timestamp}_vs_{run2_timestamp}.json"
            with open(report_path, 'w') as f:
                json.dump({
                    "baseline": run1_timestamp,
                    "current": run2_timestamp,
                    "compared_at": datetime.now().isoformat(),
                    "results": results
                }, f, indent=2)
                
            print(f"\n💾 Report saved: {report_path}")
            
    def interactive_compare(self):
        """Interactive comparison mode"""
        runs = self.list_runs()
        
        if len(runs) < 2:
            print("❌ Need at least 2 screenshot runs to compare")
            print("   Run './run-qa.sh quick' to create screenshots")
            return
            
        print("📁 Available screenshot runs:\n")
        for i, run in enumerate(runs):
            print(f"  [{i}] {run['timestamp']} ({run['count']} sites)")
            
        print()
        
        try:
            baseline_idx = int(input("Enter baseline run number [0]: ") or "0")
            current_idx = int(input("Enter current run number [1]: ") or "1")
            
            if baseline_idx >= len(runs) or current_idx >= len(runs):
                print("❌ Invalid run number")
                return
                
            self.compare_runs(
                runs[baseline_idx]['timestamp'],
                runs[current_idx]['timestamp']
            )
            
        except (ValueError, KeyboardInterrupt):
            print("\n❌ Cancelled")
            return


def main():
    comparator = ScreenshotComparator()
    
    if len(sys.argv) > 2:
        # Direct comparison mode
        comparator.compare_runs(sys.argv[1], sys.argv[2])
    else:
        # Interactive mode
        comparator.interactive_compare()


if __name__ == "__main__":
    main()

