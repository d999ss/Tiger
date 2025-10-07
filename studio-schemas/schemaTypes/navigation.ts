import {defineField, defineType} from 'sanity'

export default defineType({
  name: 'navigation',
  title: 'Site Navigation',
  type: 'document',
  fields: [
    defineField({
      name: 'title',
      title: 'Navigation Title',
      type: 'string',
      readOnly: true,
      initialValue: 'Main Navigation',
    }),
    defineField({
      name: 'logo',
      title: 'Logo Text',
      type: 'string',
      initialValue: 'TIGER BIOSCIENCES™',
    }),
    defineField({
      name: 'megaMenus',
      title: 'Mega Menu Items',
      type: 'array',
      of: [
        {
          type: 'object',
          fields: [
            {
              name: 'title',
              title: 'Menu Title',
              type: 'string',
              description: 'e.g., "Our Science", "Products", "Solutions"',
              validation: (Rule) => Rule.required(),
            },
            {
              name: 'columns',
              title: 'Menu Columns',
              type: 'array',
              of: [
                {
                  type: 'object',
                  fields: [
                    {
                      name: 'heading',
                      title: 'Column Heading',
                      type: 'string',
                      validation: (Rule) => Rule.required(),
                    },
                    {
                      name: 'links',
                      title: 'Links',
                      type: 'array',
                      of: [
                        {
                          type: 'object',
                          fields: [
                            {name: 'label', type: 'string', title: 'Link Label'},
                            {name: 'url', type: 'string', title: 'Link URL'},
                          ],
                        },
                      ],
                    },
                  ],
                  preview: {
                    select: {
                      title: 'heading',
                      links: 'links',
                    },
                    prepare({title, links}) {
                      return {
                        title: title,
                        subtitle: `${links?.length || 0} links`,
                      }
                    },
                  },
                },
              ],
              validation: (Rule) => Rule.max(4),
            },
            {
              name: 'featuredCard',
              title: 'Featured Card',
              type: 'object',
              fields: [
                {name: 'badge', type: 'string', title: 'Badge Text'},
                {name: 'title', type: 'string', title: 'Card Title'},
                {name: 'description', type: 'text', title: 'Description', rows: 2},
                {name: 'ctaText', type: 'string', title: 'CTA Button Text'},
                {name: 'ctaUrl', type: 'string', title: 'CTA Button URL'},
              ],
            },
          ],
          preview: {
            select: {
              title: 'title',
              columns: 'columns',
            },
            prepare({title, columns}) {
              return {
                title: title,
                subtitle: `${columns?.length || 0} columns`,
              }
            },
          },
        },
      ],
      validation: (Rule) => Rule.max(3),
    }),
    defineField({
      name: 'directLinks',
      title: 'Direct Links',
      type: 'array',
      of: [
        {
          type: 'object',
          fields: [
            {name: 'label', type: 'string', title: 'Link Label'},
            {name: 'url', type: 'string', title: 'Link URL'},
          ],
        },
      ],
      description: 'Simple links without dropdowns (e.g., About, Contact)',
    }),
    defineField({
      name: 'ctaButton',
      title: 'CTA Button',
      type: 'object',
      fields: [
        {name: 'text', type: 'string', title: 'Button Text'},
        {name: 'url', type: 'string', title: 'Button URL'},
      ],
    }),
  ],
  preview: {
    prepare() {
      return {
        title: 'Main Navigation',
      }
    },
  },
})

