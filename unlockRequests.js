var R1 = true
var R2 = true
var R3 = true
var R4 = true
var R5 = true

function onR1(){
    R1 = R1 == true ? false : true;
    var ele = document.getElementById("u1").innerHTML
    document.getElementById("u1").innerHTML = ele.includes("Un") ? "Locked" : "Unlocked";
}

function onR2(){
    R2 = R2 == true ? false : true;
    var ele = document.getElementById("u2").innerHTML
    document.getElementById("u2").innerHTML = ele.includes("Un") ? "Locked" : "Unlocked";
}

function onR3(){
    R3 = R3 == true ? false : true;
    var ele = document.getElementById("u3").innerHTML
    document.getElementById("u3").innerHTML = ele.includes("Un") ? "Locked" : "Unlocked";
}

function onR4(){
    R4 = R4 == true ? false : true;
    var ele = document.getElementById("u4").innerHTML
    document.getElementById("u4").innerHTML = ele.includes("Un") ? "Locked" : "Unlocked";
}

function onR5(){
    R5 = R5 == true ? false : true;
    var ele = document.getElementById("u5").innerHTML
    document.getElementById("u5").innerHTML = ele.includes("Un") ? "Locked" : "Unlocked";
}