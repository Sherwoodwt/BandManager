// passed in form will disable submit button unless all forms have some input
// formName must equal id of form,
// submit button must have id of submit
function formIsFilled(formName, elements) {
    var filledOut = true;

    for(var i = 0; i < elements.length; i++) {
        if(document.getElementById(elements[i]).value.length == 0) {
            filledOut = false;
            break;
        }
    }

    if(filledOut) {
        document.getElementById('submit').disabled = false;
    }
    else {
        document.getElementById('submit').disabled = true;
    }
}

function taskFormIsFilled() {
    var list = ['TaskTitle', 'TaskDescription'];
    formIsFilled('addTask', list);
}

function commentFormIsFilled() {
    var list = ['BodyText'];
    formIsFilled('addComment', list);
}