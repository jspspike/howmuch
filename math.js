var houston_total = 15.0;
var detroit_total = 5.0;

var houston = {'254': {'name': 'The Cheesy Poofs', 'amount': 10.0, 'img': '254.png', 'per': 0.4545454545454546}, '118': {'name': 'Robonauts', 'amount': 5.0, 'img': '118.png', 'per': 1.6666666666666665}, '?': {'name': 'New Team', 'num': '', 'per': 15.0, 'img': 'unknown.png'}};
var detroit = {'2056': {'name': 'OP Robotics', 'amount': 5.0, 'img': '2056.png', 'per': 0.0}, '?': {'name': 'New Team', 'num': '', 'per': 5.0, 'img': 'unknown.png'}};

console.log($("#254").text());

function change(key) {
    var amount = parseFloat(houston[key]["amount"]);
    var input = parseFloat($('#' + key + 'in').val());
    if (isNaN(input))
        input = 1.0;
    var total = 0;
    if(key in houston)
        total = houston_total
    else
        total = detroit_total
    $('#' + key).text(((total - amount) * (input / (input + amount))).toFixed(2));
}