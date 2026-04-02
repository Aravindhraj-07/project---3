document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('fraudForm');
    const loading = document.getElementById('loading');
    const result = document.getElementById('result');
    const predictionEl = document.getElementById('prediction');
    const confidenceFill = document.getElementById('confidenceFill');
    const confidenceEl = document.getElementById('confidence');
    const fraudProbEl = document.getElementById('fraudProb');
    const resultIcon = document.getElementById('resultIcon');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Show loading
        loading.classList.remove('hidden');
        result.classList.add('hidden');
        
        // Collect ALL 30 features
        const formData = {};
        const features = [
            'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
            'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',
            'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'
        ];
        
        features.forEach(feature => {
            const element = document.getElementById(feature);
            formData[feature] = parseFloat(element.value) || 0.0;
        });
        
        console.log('Sending data:', formData); // Debug log
        
        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            console.log('Response:', data); // Debug log
            
            // Hide loading, show result
            loading.classList.add('hidden');
            result.classList.remove('hidden');
            
            if (data.error) {
                predictionEl.textContent = `Error: ${data.error}`;
                resultIcon.innerHTML = '<i class="fas fa-exclamation-triangle"></i>';
                return;
            }
            
            // Update results
            predictionEl.textContent = data.prediction;
            confidenceEl.textContent = data.confidence.toFixed(1) + '%';
            fraudProbEl.textContent = data.fraud_probability.toFixed(2) + '%';
            
            confidenceFill.style.width = data.confidence + '%';
            
            // Update icon
            if (data.prediction === 'FRAUD') {
                resultIcon.innerHTML = '<i class="fas fa-exclamation-triangle text-danger"></i>';
                document.body.style.background = 'linear-gradient(135deg, #ff6b6b, #ee5a52)';
            } else {
                resultIcon.innerHTML = '<i class="fas fa-check-circle text-success"></i>';
                document.body.style.background = 'linear-gradient(135deg, #a8e6cf, #88d8a3)';
            }
            
        } catch (error) {
            console.error('Fetch error:', error);
            loading.classList.add('hidden');
            predictionEl.textContent = 'Connection Error';
            resultIcon.innerHTML = '<i class="fas fa-wifi-slash"></i>';
            result.classList.remove('hidden');
        }
    });
});