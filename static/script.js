function toggleCard(card) {
    // Schließt alle anderen Karten (egal ob Layer oder Info-Karte)
    const allCards = document.querySelectorAll('.layer-card.active, .description-card.active');
    
    allCards.forEach(container => {
        if (container !== card) {
            container.classList.remove('active');
        }
    });

    // Schaltet die angeklickte Karte um
    card.classList.toggle("active");
}