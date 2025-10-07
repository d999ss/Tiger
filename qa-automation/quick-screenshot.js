#!/usr/bin/env node
/**
 * Tiger CMS Quick Screenshot Tool
 * Using Terminator.js for browser automation
 */

const { Desktop } = require("terminator.js");
const fs = require("fs");
const path = require("path");

const SITES = [
  { name: "Airway Medix", path: "airway-medix.com/index.html" },
  { name: "Bellafill", path: "bellafill.com/index.html" },
  { name: "Birth Tissue Recovery", path: "birthtissuerecovery.com/index.html" },
  { name: "Encore Surgical", path: "encoresurgicalsupplies.com/index.html" },
  { name: "Extremity Care", path: "extremitycare.com/index.html" },
  { name: "Lizard Health", path: "lizard-health.com/index.html" },
  { name: "MyAveli", path: "myaveli.com/index.html" },
  { name: "Sientra", path: "sientra.com/index.html" },
  { name: "Tiger Aesthetics", path: "tiger-aesthetics.com/index.html" },
  { name: "Tiger Biosciences", path: "tigerbiosciences.com/index.html" },
  { name: "Tiger Wound Care", path: "tigerwoundcare.com/index.html" },
];

const BASE_PATH = "/Users/donnysmith/Desktop/Tiger CMS";

async function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function quickScreenshot() {
  const desktop = new Desktop();
  const timestamp = new Date().toISOString().replace(/[:.]/g, "-").slice(0, -5);
  const outputDir = path.join(BASE_PATH, "qa-automation", "screenshots", timestamp);

  // Create output directory
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  console.log("🌐 Opening Chrome browser...");
  await desktop.openApplication("chrome");
  await sleep(3000);

  const results = [];

  for (const site of SITES) {
    console.log(`\n📸 Capturing: ${site.name}`);

    try {
      // Build file URL
      const fullPath = path.join(BASE_PATH, site.path);
      const url = `file://${fullPath}`;

      // Navigate to URL
      const addressBar = await desktop.locator("role:textbox name:Address");
      await addressBar.click();
      await sleep(300);

      await desktop.pressKey("{Ctrl}a");
      await addressBar.typeText(url);
      await desktop.pressKey("{Return}");
      await sleep(2500);

      // Take screenshot
      const screenshotName = `${site.name.replace(/\s+/g, "_")}.png`;
      const screenshotPath = path.join(outputDir, screenshotName);
      await desktop.screenshot(screenshotPath);

      console.log(`✅ Saved: ${screenshotName}`);

      results.push({
        name: site.name,
        path: site.path,
        screenshot: screenshotPath,
        status: "success",
        timestamp: new Date().toISOString(),
      });
    } catch (error) {
      console.error(`❌ Error with ${site.name}:`, error.message);
      results.push({
        name: site.name,
        path: site.path,
        error: error.message,
        status: "error",
        timestamp: new Date().toISOString(),
      });
    }
  }

  // Save results JSON
  const resultsPath = path.join(outputDir, "results.json");
  fs.writeFileSync(resultsPath, JSON.stringify(results, null, 2));

  console.log(`\n✅ Complete! Screenshots saved to: ${outputDir}`);
  console.log(`📊 Results: ${resultsPath}`);

  // Print summary
  const successCount = results.filter((r) => r.status === "success").length;
  const errorCount = results.filter((r) => r.status === "error").length;
  console.log(`\n📈 Summary: ${successCount} successful, ${errorCount} errors`);
}

// Run if executed directly
if (require.main === module) {
  quickScreenshot().catch((error) => {
    console.error("Fatal error:", error);
    process.exit(1);
  });
}

module.exports = { quickScreenshot };

