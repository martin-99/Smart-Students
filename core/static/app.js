
function saveAnswer(){
    const form = document.forms.quiz
        const radios = form.elements
        const ans = Array
                     .from(radios)
                     .find(radio => radio.checked).value;
        const radio_btn = Array
                     .from(radios)
                     .find(radio => radio.checked);
        let question_id = radio_btn.name
        
     let url = `/saveans?ans=${ans}&question=${question_id}`               
    let req = new XMLHttpRequest()
    req.open('GET',url,true)
    req.send()    
    
}
let btn_save = document.getElementById("save");
        btn_save.addEventListener("click",saveAnswer)
