import {defineField, defineType} from 'sanity'

export default defineType({
  name: 'testimonialSection',
  title: 'Testimonial Section',
  type: 'object',
  fields: [
    defineField({
      name: 'sectionTitle',
      title: 'Section Title',
      type: 'string',
    }),
    defineField({
      name: 'sectionSubtitle',
      title: 'Section Subtitle',
      type: 'string',
    }),
    defineField({
      name: 'testimonials',
      title: 'Testimonials',
      type: 'array',
      of: [
        {
          type: 'object',
          fields: [
            {
              name: 'quote',
              title: 'Quote',
              type: 'text',
              rows: 4,
              validation: (Rule) => Rule.required(),
            },
            {
              name: 'authorName',
              title: 'Author Name',
              type: 'string',
              validation: (Rule) => Rule.required(),
            },
            {
              name: 'authorTitle',
              title: 'Author Title',
              type: 'string',
            },
            {
              name: 'authorOrganization',
              title: 'Author Organization',
              type: 'string',
            },
            {
              name: 'authorAvatar',
              title: 'Author Avatar',
              type: 'string',
              description: 'Initials for avatar (e.g., "MD", "PhD")',
            },
            {
              name: 'authorImage',
              title: 'Author Photo',
              type: 'image',
              options: {
                hotspot: true,
              },
            },
          ],
          preview: {
            select: {
              title: 'authorName',
              subtitle: 'authorTitle',
            },
          },
        },
      ],
      validation: (Rule) => Rule.min(1).max(4),
    }),
  ],
  preview: {
    select: {
      testimonials: 'testimonials',
    },
    prepare({testimonials}) {
      return {
        title: 'Testimonials',
        subtitle: `${testimonials?.length || 0} testimonials`,
      }
    },
  },
})

