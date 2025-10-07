import {defineField, defineType} from 'sanity'

export default defineType({
  name: 'heroSection',
  title: 'Hero Section',
  type: 'object',
  fields: [
    defineField({
      name: 'badge',
      title: 'Badge Text',
      type: 'string',
      description: 'Small badge above the title (e.g., "Product", "Research")',
    }),
    defineField({
      name: 'title',
      title: 'Hero Title',
      type: 'string',
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'subtitle',
      title: 'Hero Subtitle',
      type: 'text',
      rows: 3,
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'backgroundImage',
      title: 'Background Image',
      type: 'image',
      options: {
        hotspot: true,
      },
      fields: [
        {
          name: 'alt',
          type: 'string',
          title: 'Alternative text',
        },
      ],
    }),
    defineField({
      name: 'useGradient',
      title: 'Use Gradient Background',
      type: 'boolean',
      description: 'If true, uses gradient instead of image',
      initialValue: true,
    }),
    defineField({
      name: 'ctaButtons',
      title: 'CTA Buttons',
      type: 'array',
      of: [
        {
          type: 'object',
          fields: [
            {name: 'text', type: 'string', title: 'Button Text'},
            {name: 'url', type: 'string', title: 'Button URL'},
            {
              name: 'style',
              type: 'string',
              title: 'Button Style',
              options: {
                list: [
                  {title: 'Primary', value: 'primary'},
                  {title: 'Outline', value: 'outline'},
                ],
              },
              initialValue: 'primary',
            },
          ],
        },
      ],
      validation: (Rule) => Rule.max(2),
    }),
  ],
  preview: {
    select: {
      title: 'title',
      subtitle: 'badge',
    },
    prepare({title, subtitle}) {
      return {
        title: title || 'Hero Section',
        subtitle: subtitle || 'Hero',
      }
    },
  },
})

