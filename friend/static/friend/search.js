
$(document).ready(function() {
    $('input#id_phone_number').keyup(function(ev) {
        var key = ev.which;
        if (key < 48 || key > 57 || key != 45) {
            ev.preventDefault();
        }

        if (this.value.length > 13) {
            this.value = this.value.slice(0, -1);
            return;
        }

        this.value = this.value.replace(/^(\d{3})(\d)/, '$1-$2')
            .replace(/^(\d{3}-\d{4})(\d)/, '$1-$2');
    });
});
