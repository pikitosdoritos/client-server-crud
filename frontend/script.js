const signinForm = document.getElementById("signin")
const signupForm = document.getElementById("signup")

function switchForm(e) {
    e.preventDefault()
    signinForm.hidden =  !signinForm.hidden
    signupForm.hidden = !signupForm.hidden
}