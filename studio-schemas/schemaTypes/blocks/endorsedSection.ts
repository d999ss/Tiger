import {defineField, defineType} from 'sanity'

export default defineType({
  name: 'endorsedSection',
  title: 'Endorsed/Grid Section',
  type: 'object',
  description: 'Grid of items with titles and descriptions (e.g., Vertical Integration section)',
  fields: [
    defineField({
      name: 'label',
      title: 'Section Label',
      type: 'string',
    }),
    defineField({
      name: 'items',
      title: 'Grid Items',
      type: 'array',
      of: [
        {
          type: 'object',
          fields: [
            {
              name: 'title',
              title: 'Item Title',
              type: 'string',
              validation: (Rule) => Rule.required(),
            },
            {
              name: 'description',
              title: 'Item Description',
              type: 'text',
              rows: 3,
              validation: (Rule) => Rule.required(),
            },
          ],
          preview: {
            select: {
              title: 'title',
            },
          },
        },
      ],
      validation: (Rule) => Rule.min(2).max(6),
    }),
  ],
  preview: {
    select: {
      label: 'label',
      items: 'items',
    },
    prepare({label, items}) {
      return {
        title: label || 'Endorsed Section',
        subtitle: `${items?.length || 0} items`,
      }
    },
  },
})

