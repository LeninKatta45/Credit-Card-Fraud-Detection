function getRepeat() {
    var repeat = document.getElementsByName("uiBHK");
    for (var i in repeat) {
        if (repeat[i].checked) {
            return parseFloat(i);
        }
    }
    return -1; // Invalid Value
}

function getUsedChip() {
    var Chip = document.getElementsByName("uiBHK1");
    for (var j in Chip) {
        if (Chip[j].checked) {
            return parseFloat(j);
        }
    }
    return -1; // Invalid Value
}
function getUsedPin() {
    var pin  = document.getElementsByName("uiBHK2");
    for (var k in pin) {
        if (pin[k].checked) {
            return parseFloat(k);
        }
    }
    return -1; // Invalid Value
}
function getOnlineOrder() {
    var order = document.getElementsByName("uiBHK3");
    for (var m in order) {
        if (order[m].checked) {
            return parseFloat(m);
        }
    }
    return -1; // Invalid Value
}

function onClickedEstimatePrice() {
    var estFraud = document.getElementById("uiEstimatedPrice");
    const postData = {
        distance_from_home: parseFloat(document.getElementById("uiSqft").value),
        distance_from_last_transaction: parseFloat(document.getElementById("uiSqft1").value),
        ratio_to_median_purchase_price: parseFloat(document.getElementById("uiSqft2").value),
        repeat_retailer: getRepeat(),
        used_chip: getUsedChip(),
        used_pin_number: getUsedPin(),
        online_order: getOnlineOrder()
    };
    $.ajax({
        url: '/api/predict',
        type: 'POST',
        data: JSON.stringify(postData),
        contentType: 'application/json',
        dataType: 'json',
        success: function (data) {
            console.log(data.prediction);
            estFraud.innerHTML = "<h2>" + data.prediction + "</h2>";
        },
        error: function (xhr, status, error) {
            console.error(error);
        }
    });
    

}