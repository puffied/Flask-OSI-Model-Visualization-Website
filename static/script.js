function toggleCard(card) {
    const allCards = document.querySelectorAll('.layer-card.active, .description-card.active');
    
    allCards.forEach(container => {
        if (container !== card) {
            container.classList.remove('active');
        }
    });

    card.classList.toggle("active");
}