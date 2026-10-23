(() => {
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  if (menu && nav) {
    menu.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      menu.setAttribute('aria-expanded', String(open));
    });
  }
  const search = document.querySelector('[data-notebook-search]');
  const topic = document.querySelector('[data-notebook-topic]');
  const cards = [...document.querySelectorAll('[data-notebooks-grid] [data-item]')];
  const empty = document.querySelector('[data-no-results]');
  function update() {
    if (!cards.length) return;
    const query = (search?.value || '').trim().toLowerCase();
    const selected = (topic?.value || '').toLowerCase();
    let shown = 0;
    for (const card of cards) {
      const match = (!query || card.dataset.search.includes(query)) && (!selected || card.dataset.topic === selected);
      card.hidden = !match;
      if (match) shown++;
    }
    if (empty) empty.hidden = shown > 0;
  }
  search?.addEventListener('input', update);
  topic?.addEventListener('change', update);
})();
