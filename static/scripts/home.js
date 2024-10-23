const $ = (el) => document.querySelector(el);
const $contact = $('#contact');
const $uwu = $('#uwu');
const $footer = $('#footer');
const $gif = $('.gif');

$contact.addEventListener('click', () => {
	navigator.clipboard.writeText('okaiproject@gmail.com');
	$contact.innerHTML = 'Correo copiado en el portapapeles';
	setTimeout(() => {
		$contact.innerHTML = 'Contacto';
	}, 2000);
});

$uwu.addEventListener('click', () => {
	if ($uwu.innerHTML === 'hola?') {
		$uwu.innerHTML =
			'hola usuario! gracias por visitar nuestro proyecto, ten un corazón!';
		$gif.classList.remove('disabled');
		setTimeout(() => {
			$uwu.innerHTML = 'hola?';
			$gif.classList.add('disabled');
		}, 5000);
	}
});
