clc; clear; close();

// Daten extrahieren aus der xls datei (xlsx hat bei mir nicht funktioniert)
sheets = readxls("1g_5r.xls");
ndata = sheets(1);
data = ndata.value(2:size(ndata.value, 1), 1:3);
time = data(:,1);        // Zeit (1. Spalte)
force = data(:,2);       // Hammermessung (2. Spalte)
acceleration = data(:,3); // Beschleunigung (3. Spalte)
dim = length(time);  // Anzahl der Datenpunkte

// 2. Fourier-Transformation
force_fft = fft(force) / dim;          // Normierte FFT der Hammermessung
acceleration_fft = fft(acceleration) / dim;  // Normierte FFT der Beschleunigung

dF = 1 / (max(time) - min(time)); // Frequenzauflösung
fVec = [0:dF:(dim-1)*dF]';        // Frequenzvektor

// 3. Berechnung der Übertragungsfunktion (TF)
transfer_function = acceleration_fft ./ force_fft;  // Verhältnis von FFT der Beschleunigung zur FFT der Hammermessung
real_part = real(transfer_function); // Realteil
imag_part = imag(transfer_function); // Imaginärteil
magnitude = abs(transfer_function);  // Betrag
phase = atan(imag_part ./ real_part); // Phase der Übertragungsfunktion

// 4. Ergebnisse in eine neue Excel-Datei speichern
output_data = [time force acceleration real_part imag_part magnitude phase];
//xlsWrite("FFT_Ergebnisse2.txt", output_data);


// 5. Grafische Darstellung
// Erster Plot - Zeitsignale: Hammermessung und Beschleunigung
figure;
subplot(2, 1, 1);  // Erstes Plot: Hammermessung
plot(time, force, 'r', 'LineWidth', 1.5); // Hammermessung in rot
xlabel('Zeit [s]');
ylabel('Amplitude');
title('Hammermessung');

subplot(2, 1, 2);  // Zweites Plot: Beschleunigung
plot(time, acceleration, 'b', 'LineWidth', 1.5); // Beschleunigung in blau
xlabel('Zeit [s]');
ylabel('Amplitude');
title('Beschleunigung');

// Zweites Plot-Fenster - Frequenzspektren: Hammermessung und Beschleunigung
figure;
subplot(2, 1, 1);  // Erstes Plot: FFT Hammermessung
plot(fVec, abs(force_fft), 'r', 'LineWidth', 1.5); // FFT Hammermessung in rot
xlabel('Frequenz [Hz]');
ylabel('Amplitude');
title('FFT Hammermessung');

subplot(2, 1, 2);  // Zweites Plot: FFT Beschleunigung
plot(fVec, abs(acceleration_fft), 'b', 'LineWidth', 1.5); // FFT Beschleunigung in blau
xlabel('Frequenz [Hz]');
ylabel('Amplitude');
title('FFT Beschleunigung');

// Drittes Plot-Fenster - Übertragungsfunktion
figure;
plot(fVec, abs(transfer_function), 'g', 'LineWidth', 1.5); // Übertragungsfunktion in grün
xlabel('Frequenz [Hz]');
ylabel('Amplitude');
title('Übertragungsfunktion (Hammerkraft zu Beschleunigung)');

// Viertes Plot-Fenster - Realteil und Imaginärteil der Übertragungsfunktion
figure;
subplot(2, 1, 1);  // Realteil der Übertragungsfunktion
plot(fVec, real_part, 'g', 'LineWidth', 1.5); // Realteil in grün
xlabel('Frequenz [Hz]');
ylabel('Amplitude');
title('Realteil der Übertragungsfunktion');

subplot(2, 1, 2);  // Imaginärteil der Übertragungsfunktion
plot(fVec, imag_part, 'm', 'LineWidth', 1.5); // Imaginärteil in magenta
xlabel('Frequenz [Hz]');
ylabel('Amplitude');
title('Imaginärteil der Übertragungsfunktion');

// Fünftes Plot-Fenster - Betrag und Phase der Übertragungsfunktion
figure;
subplot(2, 1, 1);  // Betrag der Übertragungsfunktion
plot(fVec, magnitude, 'b', 'LineWidth', 1.5); // Betrag in blau
xlabel('Frequenz [Hz]');
ylabel('Amplitude');
title('Betrag der Übertragungsfunktion');

subplot(2, 1, 2);  // Phase der Übertragungsfunktion
plot(fVec, phase, 'r', 'LineWidth', 1.5); // Phase in rot
xlabel('Frequenz [Hz]');
ylabel('Phase [rad]');
title('Phase der Übertragungsfunktion');







