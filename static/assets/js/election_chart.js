var ctx = document.getElementById('pieChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Yes', 'No'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true
    }
});

var ctx = document.getElementById('barChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Yes', 'No'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true
    }
});