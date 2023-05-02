const election_title = document.getElementById("election_ttle");
const election_prompt = document.getElementById("election_prompt");
const yes_votes_number = document.getElementById("yes_votes_number").innerHTML;
const no_votes_number = document.getElementById("no_votes_number").innerHTML;

console.log(yes_votes_number, no_votes_number);
var pie = document.getElementById('pieChart').getContext('2d');
var myChart = new Chart(pie, {
    type: 'pie',
    data: {
        labels: [yes_votes_number, no_votes_number],
        datasets: [{
            label: '# of Votes',
            data: [yes_votes_number, no_votes_number],
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

var bar = document.getElementById('barChart').getContext('2d');
var myChart = new Chart(bar, {
    type: 'bar',
    data: {
        labels: ['Yes', 'No'],
        datasets: [{
            label: '# of Votes',
            data: [yes_votes_number, no_votes_number],
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
