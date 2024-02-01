$(document).ready( function () {
    $('#list-insc').DataTable(
        {
        info: false,
        paging: false,
        searching: false
        }
    );
} );


$(document).ready(function () {
        $('#confirmDeleteModal').on('show.bs.modal', function (e) { // executs when the modal opens
            var url = $(e.relatedTarget).data("id"); // gets data-id from the clicked button
            $("#confirmDeleteId").attr("href", url)
        }).on('hide.bs.modal', function (e) { // when modal closes
            $("#confirmNo").off(); // canceles the click event in button "no"
        });
});