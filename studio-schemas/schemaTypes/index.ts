// Schema types for Tiger BioSciences CMS

import homepage from './homepage'
import page from './page'
import division from './division'
import teamMember from './teamMember'
import testimonial from './testimonial'
import faq from './faq'
import siteSettings from './siteSettings'

export const schemaTypes = [
  // Singletons
  homepage,
  siteSettings,
  
  // Documents
  page,
  division,
  teamMember,
  testimonial,
  faq,
]
