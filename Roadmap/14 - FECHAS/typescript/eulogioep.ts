// Definimos algunas interfaces útiles
interface DateFormats {
    dayMonthYear: string;
    hourMinuteSecond: string;
    dayOfYear: number;
    dayOfWeek: string;
    monthName: string;
    longFormat: string;
    isoFormat: string;
    twelveHourFormat: string;
    unixTimestamp: number;
    quarterOfYear: number;
}

// Definimos algunos tipos de utilidad
type MonthName = 'Enero' | 'Febrero' | 'Marzo' | 'Abril' | 'Mayo' | 'Junio' | 
                 'Julio' | 'Agosto' | 'Septiembre' | 'Octubre' | 'Noviembre' | 'Diciembre';
type DayOfWeek = 'Domingo' | 'Lunes' | 'Martes' | 'Miércoles' | 'Jueves' | 'Viernes' | 'Sábado';

// Creamos algunas constantes con tipos
const DAYS_OF_WEEK: DayOfWeek[] = [
    'Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'
];

const MONTHS: MonthName[] = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
];

class DateCalculator {
    private currentDate: Date;
    private birthDate: Date;

    constructor(birthDate: Date) {
        this.currentDate = new Date();
        this.birthDate = birthDate;
    }

    calculateYearsBetween(): number {
        let years = this.currentDate.getFullYear() - this.birthDate.getFullYear();
        const currentMonth = this.currentDate.getMonth();
        const birthMonth = this.birthDate.getMonth();
        
        // Ajustamos si aún no hemos llegado al mes y día de nacimiento este año
        if (currentMonth < birthMonth || 
            (currentMonth === birthMonth && 
             this.currentDate.getDate() < this.birthDate.getDate())) {
            years--;
        }
        
        return years;
    }

    formatDates(): DateFormats {
        return {
            dayMonthYear: this.formatDate(this.birthDate, 'dd/MM/yyyy'),
            hourMinuteSecond: this.formatTime(this.birthDate),
            dayOfYear: this.getDayOfYear(this.birthDate),
            dayOfWeek: DAYS_OF_WEEK[this.birthDate.getDay()],
            monthName: MONTHS[this.birthDate.getMonth()],
            longFormat: this.getLongFormat(this.birthDate),
            isoFormat: this.birthDate.toISOString(),
            twelveHourFormat: this.get12HourFormat(this.birthDate),
            unixTimestamp: Math.floor(this.birthDate.getTime() / 1000),
            quarterOfYear: Math.floor(this.birthDate.getMonth() / 3) + 1
        };
    }

    private formatDate(date: Date, format: string): string {
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        
        return format
            .replace('dd', day)
            .replace('MM', month)
            .replace('yyyy', String(year));
    }

    private formatTime(date: Date): string {
        return date.toLocaleTimeString('es-ES', { 
            hour12: false,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });
    }

    private getDayOfYear(date: Date): number {
        const startOfYear = new Date(date.getFullYear(), 0, 0);
        const diff = date.getTime() - startOfYear.getTime();
        const oneDay = 1000 * 60 * 60 * 24;
        return Math.floor(diff / oneDay);
    }

    private getLongFormat(date: Date): string {
        const dayOfWeek = DAYS_OF_WEEK[date.getDay()];
        const dayOfMonth = date.getDate();
        const month = MONTHS[date.getMonth()];
        const year = date.getFullYear();
        
        return `${dayOfWeek}, ${dayOfMonth} de ${month} de ${year}`;
    }

    private get12HourFormat(date: Date): string {
        return date.toLocaleTimeString('es-ES', { hour12: true });
    }
}

// Uso del código
const birthDate = new Date(1990, 4, 15, 14, 30, 0); // Mes 4 es Mayo (0-11)
const calculator = new DateCalculator(birthDate);

// PARTE 1: Calcular años transcurridos
const yearsPassedTesting = (): void => {
    console.log('Fecha actual:', new Date().toLocaleString());
    console.log('Fecha de nacimiento:', birthDate.toLocaleString());
    console.log('Años transcurridos:', calculator.calculateYearsBetween());
};

// PARTE 2: Mostrar diferentes formatos de fecha
const showFormattedDates = (): void => {
    const formats = calculator.formatDates();
    
    console.log('\nDIFERENTES FORMATOS DE FECHA:');
    console.log('1. Día, mes y año:', formats.dayMonthYear);
    console.log('2. Hora, minuto y segundo:', formats.hourMinuteSecond);
    console.log('3. Día del año:', formats.dayOfYear);
    console.log('4. Día de la semana:', formats.dayOfWeek);
    console.log('5. Nombre del mes:', formats.monthName);
    console.log('6. Formato largo:', formats.longFormat);
    console.log('7. Formato ISO:', formats.isoFormat);
    console.log('8. Formato 12 horas:', formats.twelveHourFormat);
    console.log('9. Unix Timestamp:', formats.unixTimestamp);
    console.log('10. Trimestre del año:', formats.quarterOfYear);
};

// Ejecutamos las funciones
yearsPassedTesting();
showFormattedDates();