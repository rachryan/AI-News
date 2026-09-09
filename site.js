(function () {
    const root = document.documentElement;
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme === 'light' || savedTheme === 'dark') {
        root.setAttribute('data-theme', savedTheme);
    }

    function updateThemeButton() {
        const button = document.querySelector('.theme-toggle');
        if (!button) return;

        const isLight = root.getAttribute('data-theme') === 'light';
        button.setAttribute('aria-label', isLight ? 'Switch to dark mode' : 'Switch to light mode');
        button.title = isLight ? 'Switch to dark mode' : 'Switch to light mode';
    }

    document.addEventListener('DOMContentLoaded', function () {
        const themeButton = document.querySelector('.theme-toggle');
        const nav = document.querySelector('.site-nav');
        const menuButton = document.querySelector('.menu-toggle');
        const year = document.querySelector('[data-current-year]');

        updateThemeButton();

        if (year) {
            year.textContent = String(new Date().getFullYear());
        }

        if (themeButton) {
            themeButton.addEventListener('click', function () {
                const nextTheme = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
                root.setAttribute('data-theme', nextTheme);
                localStorage.setItem('theme', nextTheme);
                updateThemeButton();
            });
        }

        if (nav && menuButton) {
            menuButton.addEventListener('click', function () {
                const isOpen = nav.getAttribute('data-open') === 'true';
                nav.setAttribute('data-open', String(!isOpen));
                menuButton.setAttribute('aria-expanded', String(!isOpen));
            });

            nav.querySelectorAll('a').forEach(function (link) {
                link.addEventListener('click', function () {
                    nav.setAttribute('data-open', 'false');
                    menuButton.setAttribute('aria-expanded', 'false');
                });
            });
        }
    });
})();
