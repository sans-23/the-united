function toggleSieve(sievename) {
    if(sievename == "sieve1"){
        var x = document.getElementById("sieve2");
        var z = document.getElementById('b2');
        var k = document.getElementById('b1');
        x.style.display = "none";
        z.style.color = "black";
        z.style.backgroundColor = "white";
        k.style.color = "white";
        k.style.backgroundColor = "black";
    }
    else{
        var x = document.getElementById("sieve1");
        var z = document.getElementById('b1');
        var k = document.getElementById('b2');
        x.style.display = "none";
        z.style.color = "black";
        z.style.backgroundColor = "white";
        k.style.color = "white";
        k.style.backgroundColor = "black";
    }
 var y = document.getElementById(sievename);
 y.style.display = "block";
}

function toggleSlopes(slopename) {
    if(slopename == "type1"){
        var x = document.getElementById("type2");
        var y = document.getElementById("type3");
        var a = document.getElementById('b2');
        var b = document.getElementById('b1');
        var c = document.getElementById('b3');
        x.style.display = "none";
        y.style.display = "none";
        a.style.color = "black";
        a.style.backgroundColor = "white";
        b.style.color = "white";
        b.style.backgroundColor = "black";
        c.style.color = "black";
        c.style.backgroundColor = "white";
    }
    else if(slopename == "type2"){
        var x = document.getElementById("type1");
        var y = document.getElementById("type3");
        var a = document.getElementById('b1');
        var b = document.getElementById('b2');
        var c = document.getElementById('b3');
        x.style.display = "none";
        y.style.display = "none";
        a.style.color = "black";
        a.style.backgroundColor = "white";
        b.style.color = "white";
        b.style.backgroundColor = "black";
        c.style.color = "black";
        c.style.backgroundColor = "white";
    }
    else{
        var x = document.getElementById("type1");
        var y = document.getElementById("type2");
        var a = document.getElementById('b1');
        var b = document.getElementById('b2');
        var c = document.getElementById('b3');
        x.style.display = "none";
        y.style.display = "none";
        a.style.color = "black";
        a.style.backgroundColor = "white";
        b.style.color = "black";
        b.style.backgroundColor = "white";
        c.style.color = "white";
        c.style.backgroundColor = "black";
    }
 var y = document.getElementById(slopename);
 y.style.display = "block";
}

function showMass(selectedOption) {

    if(selectedOption.value=="1") {
        document.getElementById('mass1').style.display = 'none';
    } else {
        document.getElementById('mass1').style.display = 'block';
    }
}

function showMass2(selectedOption) {

    if(selectedOption.value=="1") {
        document.getElementById('mass2').style.display = 'none';
    } else {
        document.getElementById('mass2').style.display = 'block';
    }
}

var x = 0;
var array = Array();
var ShearS= Array();
var cavg=0;
var fi= Array();
var fiavg=0;
var c= Array();

function add_element_to_array()
{
array[x] = document.getElementById("Normal Stress").value;
ShearS[x]= document.getElementById("Shear Stress").value;
x++;
document.getElementById("Normal Stress").value = "";
document.getElementById("Shear Stress").value = "";

}
function Solver() {
var k= array.length;
var p=0,sum=0;
k=k*(k-1)/2;
k= Math.floor(k);
for(var i=0;i<array.length-1;i++)
{
for(var j=i+1;j<array.length;j++)
{
fi[p]=(ShearS[j]-ShearS[i])/(array[j]-array[i]);
sum+=fi[p];
 p++;
}
}
sum= sum/k;
fiavg=sum;
for(var i=0;i<array.length;i++)
{
c[i]=ShearS[i]-array[i]*sum;
cavg+=c[i];
}
cavg=cavg/(array.length);

sum = Math.atan(sum);

document.getElementById("demo").innerHTML= sum*180/3.14;

}
function cohesion() {
document.getElementById("demo2").innerHTML= cavg;

}
function display_array()
{
var e = "<hr/>";
var ee="<hr/>";
for (var y=0; y<array.length; y++)
{
e += "Normal Stress:" + y + " = " + array[y] + "<br/>";
ee+= "Shear Stress:" + y + " = " + ShearS[y] + "<br/>";
}
document.getElementById("Result").innerHTML = e;
document.getElementById("Result2").innerHTML = ee;

}
function plotdata()
{
var data = [{
      x: [0 ,5000],
      y:[cavg,5000*fiavg+cavg]
    }];
var layout = {font: {size: 18}};
var config = {responsive: true};
TESTER = document.getElementById('test');
Plotly.newPlot(TESTER, data, layout, config);
}

function add()
{
x=0;
chamberP[x] = document.getElementById("Confining Pressure").value;
Deviator[x]= document.getElementById("Max. Deviator Pressure").value;
Porewater[x]= document.getElementById("pore water Pressure").value;

x++;
document.getElementById("Confining Pressure").value = "";
document.getElementById("Max. Deviator Pressure").value = "";
document.getElementById("pore water Pressure").value = "";
}

function display()
{
var e = "<hr/>";
var ee="<hr/>";
var eee="<hr/>";
for (var y=0; y<chamberP.length; y++)
{
e += "Confining Pressure" + y + " = " + chamberP[y] + "<br/>";
ee+= "Max. Deviator Pressure" + y + " = " + Deviator[y] + "<br/>";
eee+= "pore water Pressure" + y + " = " + Porewater[y] + "<br/>";
}
document.getElementById("T1").innerHTML = e;
document.getElementById("T2").innerHTML = ee;
document.getElementById("T3").innerHTML = eee;

}