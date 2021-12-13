function incrementValue()
{
    var value = parseInt(document.getElementById('inpt').value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('inpt').value = value;
}



function decrementValue()
{
    var value = parseInt(document.getElementById('inpt').value, 10);
    value = isNaN(value) ? 0 : value;
    value--;
    document.getElementById('inpt').value = value;
}


function incrementValue2()
{
    var value = parseInt(document.getElementById('inpt2').value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('inpt2').value = value;
}



function decrementValue2()
{
    var value = parseInt(document.getElementById('inpt2').value, 10);
    value = isNaN(value) ? 0 : value;
    value--;
    document.getElementById('inpt2').value = value;
}