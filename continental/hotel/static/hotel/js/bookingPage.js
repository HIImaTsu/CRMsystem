let currentDate = new Date(2024, 2, 28); // Инициализация с датой
const scheduleContent = document.getElementById('scheduleContent');


// Обновленные данные для записей с поддержкой нескольких броней на одну дату
const entries = {
  '29.03.2024': [
    { text: 'Nurtas Almir', color: 'bg-green-300' },
    // Предполагаемая вторая запись на ту же дату
    { text: 'Забронирован', color: 'bg-red-300' }
  ],
  '30.03.2024': [
    { text: 'Nurtas Almir', color: 'bg-green-300' },
    // Предполагаемая вторая запись на ту же дату
    { text: 'Забронирован', color: 'bg-yellow-300' }
  ],
  '31.03.2024': [
    { text: 'Nurtas Almir', color: 'bg-green-300' },
    // Предполагаемая вторая запись на ту же дату
    { text: 'Забронирован', color: 'bg-yellow-300' }
  ],
  '29.03.2024': [
    { text: 'Рахат', color: 'bg-green-300' },
    // Предполагаемая вторая запись на ту же дату
    { text: 'Рахат-2', color: 'bg-yellow-300' }
  ],
  // Добавьте больше дат и записей по мере необходимости...
};

function formatDate(date) {
  const options = { day: '2-digit', month: '2-digit', year: 'numeric' };
  return date.toLocaleDateString('ru', options);
}


function populateDates() {
  const datesDiv = document.getElementById('dates');
  datesDiv.innerHTML = '';
  for (let i = 0; i < 3; i++) {
      const newDate = new Date(currentDate);
      newDate.setDate(newDate.getDate() + i);
      const dateDiv = document.createElement('div');
      // Increase horizontal margin using mx-2 or mx-4 for more space
      dateDiv.className = 'px-12 py-1 mx-12 rounded bg-white'; // Changed mx-1 to mx-4
      dateDiv.textContent = formatDate(newDate);
      datesDiv.appendChild(dateDiv);
  }
}

// Вызываем функцию при обновлении дат




function populateSchedule() {
  scheduleContent.innerHTML = ''; // Очистка расписания
  const maxEntriesPerDay = 3; // Максимальное количество блоков бронирования на дату

  for (let i = 0; i < 3; i++) {
      const newDate = new Date(currentDate);
      newDate.setDate(newDate.getDate() + i);
      const entryDate = formatDate(newDate);
      const columnDiv = document.createElement('div');
      columnDiv.className = 'flex flex-col items-center gap-2 '; // Добавлен класс gap для пространства между блоками

      const dayEntries = entries[entryDate] || [];
      dayEntries.forEach(({text, color}) => {
          const entryDiv = document.createElement('div');
          entryDiv.className = `${color} rounded px-4 py-2 my-1 w-full`;
          entryDiv.textContent = text;
          columnDiv.appendChild(entryDiv);
      });

      // Добавление дополнительных блоков для заполнения пространства
      for (let j = dayEntries.length; j < maxEntriesPerDay; j++) {
          const fillerDiv = document.createElement('div');
          fillerDiv.className = 'bg-gray-300 rounded px-4 py-2 my-1 w-full'; // Используйте желаемый цвет для заполнения
          fillerDiv.textContent = 'Пусто'; // Текст для заполнителя, можно оставить пустым
          columnDiv.appendChild(fillerDiv);
      }

      scheduleContent.appendChild(columnDiv);
  }
}



// Update function that repopulates dates and schedule
function update() {
  populateDates();
  populateSchedule();
}

// Navigation button events
document.getElementById('prevDate').addEventListener('click', () => {
  currentDate.setDate(currentDate.getDate() - 1);
  update();
});

document.getElementById('nextDate').addEventListener('click', () => {
  currentDate.setDate(currentDate.getDate() + 1);
  update();
});

// Initialize
update();
updateDatesLayout();

