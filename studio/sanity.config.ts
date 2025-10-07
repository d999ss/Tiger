import {defineConfig} from 'sanity'
import {structureTool} from 'sanity/structure'
import {visionTool} from '@sanity/vision'
import {schemaTypes} from './schemaTypes'

export default defineConfig({
  name: 'default',
  title: 'Tiger BioSciences CMS',

  projectId: '0nxq33lj',
  dataset: 'production',

  plugins: [
    structureTool({
      structure: (S) =>
        S.list()
          .title('Content Management')
          .items([
            // Singletons
            S.listItem()
              .title('🏠 Homepage')
              .child(
                S.document()
                  .schemaType('homepage')
                  .documentId('homepage')
              ),
            S.listItem()
              .title('🧭 Navigation')
              .child(
                S.document()
                  .schemaType('navigation')
                  .documentId('navigation')
              ),
            S.listItem()
              .title('⚙️ Site Settings')
              .child(
                S.document()
                  .schemaType('siteSettings')
                  .documentId('siteSettings')
              ),
            
            S.divider(),
            
            // Documents
            S.listItem()
              .title('📄 Pages')
              .child(
                S.documentTypeList('page')
                  .title('All Pages')
              ),
            S.listItem()
              .title('👥 Team Members')
              .child(
                S.documentTypeList('teamMember')
                  .title('Team Members')
              ),
            S.listItem()
              .title('💬 Testimonials')
              .child(
                S.documentTypeList('testimonial')
                  .title('Testimonials')
              ),
            S.listItem()
              .title('❓ FAQs')
              .child(
                S.documentTypeList('faq')
                  .title('FAQ Items')
              ),
            S.listItem()
              .title('🏢 Divisions')
              .child(
                S.documentTypeList('division')
                  .title('Company Divisions')
              ),
          ]),
    }),
    visionTool(),
  ],

  schema: {
    types: schemaTypes,
  },
})
