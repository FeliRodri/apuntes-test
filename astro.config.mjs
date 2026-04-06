// @ts-check
import starlight from '@astrojs/starlight';
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Mi Documentación',
			defaultLocale: 'root',
			locales: {
				root: { label: 'Español', lang: 'es' },
			},
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com' },
			],
			customCss: ['./src/styles/custom.css'],
			head: [
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
					items: [
						{ label: 'Introducción', slug: 'clases/introduccion' },
						{
							label: 'Programación',
							items: [
								{ label: 'Fundamentos', slug: 'clases/programacion/fundamentos' },
								{ label: 'POO', slug: 'clases/programacion/poo' },
							],
						},
						{
							label: 'Bases de Datos',
							items: [
								{ label: 'Introducción', slug: 'clases/bases-de-datos/introduccion' },
								{ label: 'SQL Básico', slug: 'clases/bases-de-datos/sql-basico' },
								{ label: 'Semántica', slug: 'clases/bases-de-datos/semantica' },
								{ label: 'Fundamentos', slug: 'clases/bases-de-datos/fundamentos' },
								{ label: 'Fundamentos-Imagenes', slug: 'clases/bases-de-datos/fundamentostestimagenes' },
							],
						},
					],
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
});
