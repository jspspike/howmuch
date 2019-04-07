var houston_total = {{ houston_total }};
var detroit_total = {{ detroit_total }};

var houston = {{ houston }};
var detroit = {{ detroit }};

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
