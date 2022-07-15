var x = 0;
var x1=0;
var array = Array();
var ShearS= Array();
var cavg=0;
var fi= Array();
var fiavg=0;
var c= Array();
var chamberP= Array();
var Deviator =Array();
var Porewater= Array();
var totalstress= Array();
var effectivestress = Array();
var r_totalstr= Array();
var c_totalstr= Array();
var r_effstr= Array();
var c_effstr= Array();
var chamberReduce= Array();
var mtotal=0;
var meffective=0;
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
   var div1=document.createElement("div");
  
   div1.style.background = "#43C6DB";
   div1.style.color = "black";
   div1.style.padding="10px";
   div1.style.fontSize="20px";
   div1.style.display= "inline-block";
   div1.style.margin="10px";
   div1.innerHTML = "Angle of friction:- "+sum*180/3.14;
      document.getElementById("demo").appendChild(div1);
  
}
function cohesion() {
  var div1=document.createElement("div");
  
   div1.style.background = "#566D7E";
   div1.style.color = "black";
   div1.style.padding="10px";
   div1.style.fontSize="20px";
   div1.style.display= "inline-block";
   div1.style.margin="10px";
   div1.innerHTML = "Cohesion intercept:- "+cavg;
   document.getElementById("demo2").appendChild(div1);

}
function display_array()
{
  
   
     e = "Normal Stress(" + x + "): = " + array[x-1] + "<br/>";
    ee= "Shear Stress(" + x + "): = " + ShearS[x-1] + "<br/>";
 
   
   var div1=document.createElement("div");
  
div1.style.background = "#43C6DB";
div1.style.color = "black";
div1.style.padding="10px";
div1.style.fontSize="20px";
div1.style.display= "inline-block";
div1.innerHTML = e;
   document.getElementById("Result").appendChild(div1);
 
   var div2=document.createElement("div");
   
   div2.style.background = "#008080";
   div2.style.color = "black";
   div2.style.display= "inline-block";
   div2.style.padding="10px";
   div2.style.fontSize="20px";
   div2.innerHTML = ee;
   document.getElementById("Result2").appendChild(div2);

   
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
 chamberP[x1] = document.getElementById("Confining Pressure").value;
 Deviator[x1]= document.getElementById("Max. Deviator Pressure").value;
 Porewater[x1]= document.getElementById("pore water Pressure").value;
 
 x1++;
 document.getElementById("Confining Pressure").value = "";
document.getElementById("Max. Deviator Pressure").value = "";
 document.getElementById("pore water Pressure").value = "";
}

function display()
{
  e = "Confining Pressure(" + x1 + ") = " + chamberP[x1-1] + "<br/>";
    ee= "Max. Deviator Pressure(" + x1 + ") = " + Deviator[x1-1] + "<br/>";
 eee="pore water Pressure(" + x1 + ") = " + Porewater[x1-1] + "<br/>";
   
   var div1=document.createElement("div");
  
div1.style.background = "#43C6DB";
div1.style.color = "black";
div1.style.padding="10px";
div1.style.fontSize="20px";
div1.style.display= "inline-block";
div1.innerHTML = e;
   document.getElementById("T1").appendChild(div1);
 
   var div2=document.createElement("div");
   
   div2.style.background = "#566D7E";
   div2.style.color = "black";
   div2.style.display= "inline-block";
   div2.style.padding="10px";
   div2.style.fontSize="20px";
   div2.innerHTML = ee;
   document.getElementById("T2").appendChild(div2);
   var div3=document.createElement("div");
   
   div3.style.background = "#008080";
   div3.style.color = "black";
   div3.style.display= "inline-block";
   div3.style.padding="10px";
   div3.style.fontSize="20px";
   div3.innerHTML = eee;
   document.getElementById("T3").appendChild(div3);
   
   
}

function rc_calculator()

{ 
 
 
  for (var i=0;i< chamberP.length;i++)
  {
    totalstress[i]= chamberP[i]+Deviator[i];
    effectivestress[i]=totalstress[i]-Porewater[i];
    chamberReduce[i]=chamberP[i]-Porewater[i];
    r_totalstr[i]=(totalstress[i]-chamberP[i])/2;
    c_totalstr[i]=r_totalstr[i]+chamberP[i];
    r_effstr[i]=(effectivestress[i]-chamberReduce[i])/2;
    c_effstr[i]=r_effstr[i]+chamberReduce[i];
  }

  
   var mavg1=slope();
 
    mavg=Math.asin(mavg1);
    mtotal=mavg1;
    
    var div1=document.createElement("div");
  
div1.style.background = "#43C6DB";
div1.style.color = "black";
div1.style.padding="10px";
div1.style.fontSize="20px";
div1.style.display= "inline-block";
div1.style.margin="10px";
div1.innerHTML = "Angle of friction:- "+Math.atan(mavg1)*180/3.14 ;
   document.getElementById("demo3").appendChild(div1);
    
}
function slope()
{

    var mavg2=0;
    var m= Array();
   
    for(var i=0;i<chamberP.length-1;i++)
    {
      
      m[i]= (r_totalstr[i+1]-r_totalstr[i])/(c_totalstr[i+1]-c_totalstr[i]);
      mavg2+=m[i];
      // alert(mavg2);
    }
    
    
    return mavg2/(chamberP.length-1);
}

function intercept()
{
  
    exp_av=1000;
    exp=Array();
  
    for(var i=0;i<chamberP.length-1;i++)
    {
     
        exp[i]=(c_totalstr[i]*r_totalstr[i+1]-c_totalstr[i+1]*r_totalstr[i])/(r_totalstr[i+1]-r_totalstr[i]);
        exp_av=Math.min(exp_av,exp[i]);
        
      }
    return exp_av;
        
}
var extend= totalstress[totalstress.length-1]+50;

function c1_totalstr()
{ var exp_av;
  for (var i=0;i< chamberP.length;i++)
  {
    totalstress[i]= chamberP[i]+Deviator[i];
    effectivestress[i]=totalstress[i]-Porewater[i];
    chamberReduce[i]=chamberP[i]-Porewater[i];
    r_totalstr[i]=(totalstress[i]-chamberP[i])/2;
    c_totalstr[i]=r_totalstr[i]+chamberP[i];
    r_effstr[i]=(effectivestress[i]-chamberReduce[i])/2;
    c_effstr[i]=r_effstr[i]+chamberReduce[i];
  }
    exp_av=intercept();
    var div1=document.createElement("div");
  
div1.style.background = "#566D7E";
div1.style.color = "black";
div1.style.padding="10px";
div1.style.fontSize="20px";
div1.style.display= "inline-block";
div1.style.margin="10px";
div1.innerHTML = "Cohesion Intercept:- "+-exp_av*mtotal;
   document.getElementById("demo4").appendChild(div1);
    
   

}
function fi_effstr()
{   var mef;
  for (var i=0;i< chamberP.length;i++)
  {
    totalstress[i]= chamberP[i]+Deviator[i];
    effectivestress[i]=totalstress[i]-Porewater[i];
    chamberReduce[i]=chamberP[i]-Porewater[i];
    r_totalstr[i]=(totalstress[i]-chamberP[i])/2;
    c_totalstr[i]=r_totalstr[i]+chamberP[i];
    r_effstr[i]=(effectivestress[i]-chamberReduce[i])/2;
    c_effstr[i]=r_effstr[i]+chamberReduce[i];
  }
    mef=slope();
 
    meffective = Math.asin(mef);
   
    
    var div1=document.createElement("div");
  
div1.style.background = "#43C6DB";
div1.style.color = "black";
div1.style.padding="10px";
div1.style.fontSize="20px";
div1.style.display= "inline-block";
div1.style.margin="10px";
div1.innerHTML = "Angle of friction:- "+Math.atan(mef)*180/3.14 ;

   document.getElementById("demo5").appendChild(div1);
    
  

}
function c1_effstr()
{
  for (var i=0;i< chamberP.length;i++)
  {
    totalstress[i]= chamberP[i]+Deviator[i];
    effectivestress[i]=totalstress[i]-Porewater[i];
    chamberReduce[i]=chamberP[i]-Porewater[i];
    r_totalstr[i]=(totalstress[i]-chamberP[i])/2;
    c_totalstr[i]=r_totalstr[i]+chamberP[i];
    r_effstr[i]=(effectivestress[i]-chamberReduce[i])/2;
    c_effstr[i]=r_effstr[i]+chamberReduce[i];
  }
   var eef=0;
eef=intercept();

var div1=document.createElement("div");
  
div1.style.background = "#566D7E";
div1.style.color = "black";
div1.style.padding="10px";
div1.style.fontSize="20px";
div1.style.display= "inline-block";
div1.style.margin="10px";
div1.innerHTML = "Cohesion Intercept:- "+-eef*meffective;
   document.getElementById("demo6").appendChild(div1);
    

}
