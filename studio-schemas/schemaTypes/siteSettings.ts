import {defineField, defineType} from 'sanity'

export default defineType({
  name: 'siteSettings',
  title: 'Site Settings',
  type: 'document',
  fields: [
    defineField({
      name: 'siteName',
      title: 'Site Name',
      type: 'string',
      initialValue: 'Tiger BioSciences™',
    }),
    defineField({
      name: 'tagline',
      title: 'Tagline',
      type: 'string',
      initialValue: 'Elevate healthcare with a human touch',
    }),
    defineField({
      name: 'address',
      title: 'Address',
      type: 'object',
      fields: [
        {name: 'street', type: 'string', title: 'Street Address'},
        {name: 'city', type: 'string', title: 'City'},
        {name: 'state', type: 'string', title: 'State'},
        {name: 'zip', type: 'string', title: 'ZIP Code'},
      ],
    }),
    defineField({
      name: 'phone',
      title: 'Phone Number',
      type: 'string',
      initialValue: '(+1) 888 665 5005',
    }),
    defineField({
      name: 'email',
      title: 'Email',
      type: 'string',
    }),
    defineField({
      name: 'socialLinks',
      title: 'Social Media Links',
      type: 'object',
      fields: [
        {name: 'linkedin', type: 'url', title: 'LinkedIn'},
        {name: 'twitter', type: 'url', title: 'Twitter'},
        {name: 'facebook', type: 'url', title: 'Facebook'},
      ],
    }),
    defineField({
      name: 'footerText',
      title: 'Footer Copyright Text',
      type: 'string',
      initialValue: '© 2025 Copyright Tiger BioSciences. Realized by Cloud54.',
    }),
    defineField({
      name: 'seo',
      title: 'Default SEO',
      type: 'object',
      fields: [
        {name: 'defaultTitle', type: 'string', title: 'Default Page Title'},
        {name: 'defaultDescription', type: 'text', title: 'Default Meta Description'},
        {name: 'ogImage', type: 'image', title: 'Default Social Share Image'},
      ],
    }),
  ],
  preview: {
    prepare() {
      return {
        title: 'Site Settings',
      }
    },
  },
})
