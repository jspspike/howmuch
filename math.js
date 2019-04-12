var houston_total = 35.0;
var detroit_total = 5.0;

var houston = {'254': {'name': 'The Cheesy Poofs', 'amount': 10.0, 'img': '254.png', 'per': 2.272727272727273}, '118': {'name': 'Robonauts', 'amount': 5.0, 'img': '118.png', 'per': 5.0}, '1619': {'name': 'Up-A-Creek Robotics', 'amount': 5.0, 'img': '1619.jpg', 'per': 5.0}, '3310': {'name': 'Black Hawk Robotics', 'amount': 5.0, 'img': '3310.png', 'per': 5.0}, '148': {'name': 'Robowranglers', 'amount': 5.0, 'img': '148.png', 'per': 5.0}, '1323': {'name': 'MadTown Robotics', 'amount': 5.0, 'img': '1323.jpg', 'per': 5.0}, '?': {'name': 'New Team', 'num': '', 'per': 35.0, 'img': 'unknown.png'}};
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
    $('#' + key).text((total - amount) * (input / (input + amount)).toFixed(2));
}