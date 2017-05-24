// Wait for the DOM to be ready
$(function() {
    $("form").validate({
        errorClass: "validation",
        // Specify validation rules
        rules: {
            name: {
                required: true,
                minlength: 4
            },
            email: {
                required: true,
                // Specify that email should be validated
                // by the built-in "email" rule
                email: true
            },
            subject: {
                required: true,
                minlength: 4
            },
            message: "required"
        },
        // Specify validation error messages
        messages: {
            name: "Please enter at least 4 chars",
            email: "Please enter a valid email address",
            subject: "Please enter at least 4 chars",
            message: "Please enter a message"
        },
        errorPlacement: function (error, element) {
            error.insertAfter(element)
        },
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
        submitHandler: function(form) {
            form.submit();
        }
    });
});