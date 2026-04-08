// @ts-check
import starlight from '@astrojs/starlight';
import { defineConfig } from 'astro/config';
import rehypeKatex from 'rehype-katex';
import remarkMath from 'remark-math';

// https://astro.build/config
export default defineConfig({
	devToolbar: {
		enabled: false,
	},
	integrations: [
		starlight({
			title: 'Mis Apuntes',
			defaultLocale: 'root',
			locales: {
				root: { label: 'Español', lang: 'es' },
			},
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/FeliRodri/apuntes-test' },
			],
			customCss: ['./src/styles/custom.css'],
			head: [
				{
					tag: 'link',
					attrs: {
						rel: 'stylesheet',
						href: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css',
					},
				},
				{
					tag: 'style',
					content: `
						:root, :root[data-theme='dark'] { 
							--sl-color-bg: #0d1117 !important; 
							--sl-color-bg-nav: rgba(11, 15, 20, 0.85) !important; 
							--sl-color-bg-sidebar: #0b0f14 !important; 
						}
						:root[data-theme='light'] { 
							--sl-color-bg: #ffffff !important; 
							--sl-color-bg-nav: rgba(255, 255, 255, 0.85) !important; 
							--sl-color-bg-sidebar: #f8f9fa !important; 
						}
					`
				}
			],
			sidebar: [
				{
					label: 'Inicio',
					items: [
						{ label: 'Guía de Uso', slug: 'guia' },
					],
				},
				{
					label: 'Clases',
					autogenerate: { directory: 'clases' },
				},
				{
					label: 'Proyectos',
					items: [
						{ label: 'Introducción', slug: 'proyectos/introduccion' },
						{
							label: 'Portfolio',
							items: [
								{ label: 'Descripción', slug: 'proyectos/portfolio/descripcion' },
								{ label: 'Arquitectura', slug: 'proyectos/portfolio/arquitectura' },
							],
						},
					],
				},
			],
		}),
	],
	markdown: {
		remarkPlugins: [remarkMath],
		rehypePlugins: [rehypeKatex],
	},
});
