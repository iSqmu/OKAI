const cookies = document.cookie;

if (!cookies.includes('OKAI-gestus')) {
	introJs()
		.setOptions({
			steps: [
				{
					title: 'Bienvenido a OKAI Gestus!',
					intro: 'Te daremos una introducción a la aplicación.',
				},
				{
					title: 'Video en vivo',
					intro: 'Aquí puedes ver el video en vivo',
					element: '#video-img',
				},
				{
					title: 'Opciones',
					intro: 'Aquí puedes ver las opciones de la aplicación.',
					element: '#options',
				},
				{
					title: 'Texto',
					intro:
						'Aquí puedes escribir el texto que quieras tanto con el teclado como con los gestos.',
					element: '#input-text',
				},
				{
					title: 'Escala de grises',
					intro:
						'Si quieres que la aplicación muestre el video en blanco y negro, puedes activar esta opción.',
					element: '#grayScale',
				},
				{
					title: 'Detección de colores',
					intro:
						'Si quieres que la aplicación muestre los colores del guante, puedes activar esta opción.',
					element: '#colors-det',
				},
				{
					title: 'Cerrar',
					intro:
						'Si quieres cerrar la aplicación, puedes hacerlo con este botón.',
					element: '#exitbtn',
				},
				{
					title: '¿Estás listo?',
					intro: 'Vamos a probar la aplicación.',
				},
				{
					title: 'Dale click aquí',
					intro:
						'Aquí es donde vamos a escribir para probarlo, necesitamos que esté activo y listo para recibir el texto.',
					element: '#input-text textarea',
				},
				{
					title: 'Probemos las consonantes.',
					intro:
						'Pon la mano derecha a la vista de la camara, dependiendo de la cantidad de dedos que se muestren será una letra u otra.',
					element: '#video-img',
				},
				{
					title: 'Probemos las vocales.',
					intro:
						'Pon la mano izquierda a la vista de la camara, funciona igual que la anterior.',
					element: '#video-img',
				},
				{
					title: '¡Listo!',
					intro:
						'¡Ya sabes usar OKAI Gestus!, puedes probar escribiendo en otro sitio o aplicación.',
				},
			],
		})
		.start();
	document.cookie = 'OKAI-gestus=true';
}
