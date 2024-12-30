// On page load, set min and max for start/end datetime fields:
window.addEventListener('DOMContentLoaded', () => {
    const now = new Date();
    const endTime = new Date(now.getTime() + 3 * 60 * 60 * 1000);
    const fourDaysLater = new Date(now.getTime() + 4 * 24 * 60 * 60 * 1000);

    // Format as YYYY-MM-DDTHH:MM for datetime-local
    const pad = (n) => n.toString().padStart(2, '0');

    function toDateTimeLocalString(date) {
      const year = date.getFullYear();
      const month = pad(date.getMonth() + 1);
      const day = pad(date.getDate());
      const hour = pad(date.getHours());
      const minute = pad(date.getMinutes());
      return `${year}-${month}-${day}T${hour}:${minute}`;
    }

    const startInput = document.getElementById('start_datetime');
    const endInput = document.getElementById('end_datetime');

    startInput.min = toDateTimeLocalString(now);
    startInput.max = toDateTimeLocalString(fourDaysLater);

    endInput.min = toDateTimeLocalString(now);
    endInput.max = toDateTimeLocalString(fourDaysLater);

    // Optionally, set default values as the earliest times
    startInput.value = toDateTimeLocalString(now);
    endInput.value = toDateTimeLocalString(endTime);
  });