import {defineField, defineType} from 'sanity'

export default defineType({
  name: 'ctaSection',
  title: 'Call-to-Action Section',
  type: 'object',
  fields: [
    defineField({
      name: 'title',
      title: 'CTA Title',
      type: 'string',
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'description',
      title: 'CTA Description',
      type: 'text',
      rows: 3,
    }),
    defineField({
      name: 'buttons',
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
                  {title: 'Light', value: 'light'},
                  {title: 'Outline', value: 'outline'},
                ],
              },
              initialValue: 'light',
            },
          ],
        },
      ],
      validation: (Rule) => Rule.max(2),
    }),
    defineField({
      name: 'backgroundColor',
      title: 'Background',
      type: 'string',
      options: {
        list: [
          {title: 'Red Gradient', value: 'gradient'},
          {title: 'Dark', value: 'dark'},
        ],
      },
      initialValue: 'gradient',
    }),
  ],
  preview: {
    select: {
      title: 'title',
    },
    prepare({title}) {
      return {
        title: title || 'CTA Section',
      }
    },
  },
})

