document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predictionForm');
    const resultCard = document.getElementById('resultCard');
    const calorieValue = document.getElementById('calorieValue');
    const resultFeedback = document.getElementById('resultFeedback');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Animate button
        const btn = form.querySelector('.cta-btn');
        const originalText = btn.innerHTML;
        btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Calculating...';
        btn.disabled = true;

        // Gather data
        const formData = {
            gender: form.querySelector('input[name="gender"]:checked').value,
            age: document.getElementById('age').value,
            height: document.getElementById('height').value,
            weight: document.getElementById('weight').value,
            duration: document.getElementById('duration').value,
            heart_rate: document.getElementById('heart_rate').value,
            body_temp: document.getElementById('body_temp').value
        };

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();

            if (data.success) {
                // Show Result
                resultCard.classList.remove('hidden');
                
                // Animate numbers
                let start = 0;
                const end = data.calories;
                const duration = 1000;
                const startTime = performance.now();

                function update(currentTime) {
                    const elapsed = currentTime - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    
                    // Ease out quart
                    const ease = 1 - Math.pow(1 - progress, 4);
                    
                    const currentVal = start + (end - start) * ease;
                    calorieValue.textContent = currentVal.toFixed(1);

                    if (progress < 1) {
                        requestAnimationFrame(update);
                    }
                }
                requestAnimationFrame(update);

                // Feedback
                if (end > 500) {
                    resultFeedback.textContent = "Incredible intensity! You're on fire! 🔥";
                } else if (end > 250) {
                    resultFeedback.textContent = "Solid workout! Keep it up. 💪";
                } else {
                    resultFeedback.textContent = "Nice start! Consistency is key. 🌱";
                }

                // Scroll to result
                resultCard.scrollIntoView({ behavior: 'smooth' });

            } else {
                alert('Error: ' + data.error);
            }

        } catch (error) {
            console.error('Error:', error);
            alert('Something went wrong. Please try again.');
        } finally {
            btn.innerHTML = originalText;
            btn.disabled = false;
        }
    });
});
