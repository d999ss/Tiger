import {defineField, defineType} from 'sanity'

export default defineType({
  name: 'statsSection',
  title: 'Stats Section',
  type: 'object',
  fields: [
    defineField({
      name: 'stats',
      title: 'Statistics',
      type: 'array',
      of: [
        {
          type: 'object',
          fields: [
            {
              name: 'number',
              title: 'Stat Number',
              type: 'string',
              description: 'e.g., "15", "50+", "100+", "500+"',
              validation: (Rule) => Rule.required(),
            },
            {
              name: 'label',
              title: 'Stat Label',
              type: 'string',
              validation: (Rule) => Rule.required(),
            },
            {
              name: 'animated',
              title: 'Animate Counter',
              type: 'boolean',
              description: 'If number is numeric, animate counting up',
              initialValue: true,
            },
          ],
          preview: {
            select: {
              number: 'number',
              label: 'label',
            },
            prepare({number, label}) {
              return {
                title: `${number}`,
                subtitle: label,
              }
            },
          },
        },
      ],
      validation: (Rule) => Rule.min(2).max(4),
    }),
    defineField({
      name: 'darkBackground',
      title: 'Dark Background',
      type: 'boolean',
      description: 'Use dark background with white text',
      initialValue: true,
    }),
  ],
  preview: {
    select: {
      stats: 'stats',
    },
    prepare({stats}) {
      return {
        title: 'Stats Section',
        subtitle: `${stats?.length || 0} stats`,
      }
    },
  },
})

