import {defineField, defineType} from 'sanity'

export default defineType({
  name: 'homepage',
  title: 'Homepage',
  type: 'document',
  fields: [
    defineField({
      name: 'badge',
      title: 'Hero Badge',
      type: 'string',
      description: 'Small badge text above main title',
      initialValue: 'The First of Its Kind',
    }),
    defineField({
      name: 'title',
      title: 'Hero Title',
      type: 'string',
      description: 'Main homepage headline',
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'subtitle',
      title: 'Hero Subtitle',
      type: 'text',
      rows: 3,
      description: 'Description text below the title',
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'ctaPrimary',
      title: 'Primary CTA Button',
      type: 'object',
      fields: [
        {name: 'text', type: 'string', title: 'Button Text'},
        {name: 'link', type: 'string', title: 'Link URL'},
      ],
    }),
    defineField({
      name: 'ctaSecondary',
      title: 'Secondary CTA Button',
      type: 'object',
      fields: [
        {name: 'text', type: 'string', title: 'Button Text'},
        {name: 'link', type: 'string', title: 'Link URL'},
      ],
    }),
    defineField({
      name: 'integrationTitle',
      title: 'Integration Section Title',
      type: 'string',
      initialValue: 'The Tiger Way: The Power of Vertical Integration',
    }),
    defineField({
      name: 'integrationItems',
      title: 'Integration Items',
      type: 'array',
      of: [
        {
          type: 'object',
          fields: [
            {name: 'title', type: 'string', title: 'Title'},
            {name: 'description', type: 'text', title: 'Description'},
          ],
        },
      ],
      validation: (Rule) => Rule.max(4),
    }),
    defineField({
      name: 'divisionsTitle',
      title: 'Divisions Section Title',
      type: 'string',
    }),
    defineField({
      name: 'divisionsSubtitle',
      title: 'Divisions Section Subtitle',
      type: 'text',
    }),
  ],
  preview: {
    prepare() {
      return {
        title: 'Homepage Content',
      }
    },
  },
})
