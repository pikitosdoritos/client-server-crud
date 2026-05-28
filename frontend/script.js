const signinForm = document.getElementById("signin")
const signupForm = document.getElementById("signup")

function switchForm(e) {
    e.preventDefault()
    signinForm.hidden =  !signinForm.hidden
    signupForm.hidden = !signupForm.hidden
}

function handleSignIn(e) {
    e.preventDefault()
    const data = Object.fromEntries(new FormData(signinForm))
    const init = {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(data)}

    fetch("/login/user", init)
}

function handleSignUp(e) {
    e.preventDefault()
    const data = Object.fromEntries(new FormData(signupForm))
    const init = {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(data)}

    fetch("/register/user", init)
}