const imgpaths=["rm1.jpg","rm2.jpg","rm3.jpg","rm4.jpg"];
let index=1;

function sc(){
        index=(index+1)%imgpaths.length;
        const scroll=document.getElementById("header");
        const scrollindex=imgpaths[index];
        scroll.style.backgroundImage=`url('${scrollindex}')`;
}
setInterval(sc,2000)


const imgpath=["nabh.png","nabl.jpg","ammd.jpg"];
let ind=1;
function scll(){
        ind=(ind+1)%imgpath.length;
        const roll=document.getElementById("accimg")
        const scind=imgpath[ind];
        roll.src=scind;
}
setInterval(scll,3000)