
// var u2 = document.getElementById("u2").innerHTML
// var u3 = document.getElementById("u3").innerHTML
// var u4 = documnet.getElementById("u4").innerHTML
// var u5 = document.getElementById("u5").innerHTML


function onOpen(){
    document.getElementById("u1").innerHTML = localStorage.getItem("status1");
    document.getElementById("u2").innerHTML = localStorage.getItem("status2");
    document.getElementById("u3").innerHTML = localStorage.getItem("status3");
    document.getElementById("u4").innerHTML = localStorage.getItem("status4");
    document.getElementById("u5").innerHTML = localStorage.getItem("status5");
}

function onR1(){
    var r1 = document.getElementById("u1").innerHTML
    var flip = r1.includes("Un") ? "Locked" : "Unlocked";
    
    localStorage.setItem("status1", flip);
    document.getElementById("u1").innerHTML = flip;
}

function onR2(){
    var r2 = document.getElementById("u2").innerHTML
    var flip = r2.includes("Un") ? "Locked" : "Unlocked";
    
    localStorage.setItem("status2", flip);
    document.getElementById("u2").innerHTML = flip;
}

function onR3(){
    var r3 = document.getElementById("u3").innerHTML
    var flip = r3.includes("Un") ? "Locked" : "Unlocked";
    
    localStorage.setItem("status3", flip);
    document.getElementById("u3").innerHTML = flip;
}

function onR4(){
    var r4 = document.getElementById("u4").innerHTML
    var flip = r4.includes("Un") ? "Locked" : "Unlocked";
    
    localStorage.setItem("status4", flip);
    document.getElementById("u4").innerHTML = flip;
}

function onR5(){
    var r5 = document.getElementById("u5").innerHTML
    var flip = r5.includes("Un") ? "Locked" : "Unlocked";
    
    localStorage.setItem("status5", flip);
    document.getElementById("u5").innerHTML = flip;
}