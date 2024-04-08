# Python
% Definicja funkcji Lapunowa V(x1, x2) = x1^2 + x2^2
V = @(x1, x2) x1.^2 + x2.^2;

% Tworzenie siatki punktów (x1, x2) do wykresu
[x1, x2] = meshgrid(-2:0.1:2, -2:0.1:2);

% Obliczanie wartości funkcji V(x1, x2) na siatce
values = V(x1, x2);

% Rysowanie konturów funkcji Lapunowa V(x1, x2)
figure;
contour(x1, x2, values, 20); % 20 poziomów konturów

hold on;

% Rysowanie wektorów gradientu ∇V(x1, x2) = (2*x1, 2*x2) w wybranych punktach
points = [1 1; -1 1; 0 -2]; % Przykładowe punkty (x1, x2)

for i = 1:size(points, 1)
    x1_point = points(i, 1);
    x2_point = points(i, 2);
    
    % Obliczanie wartości gradientu w punkcie (x1_point, x2_point)
    gradient_x = 2 * x1_point;
    gradient_y = 2 * x2_point;
    
    % Rysowanie wektora gradientu w punkcie (x1_point, x2_point)
    quiver(x1_point, x2_point, gradient_x, gradient_y, 'r', 'LineWidth', 2);
end

% Dodanie tytułu i etykiet osi
title('Funkcja Lapunowa V(x_1, x_2) = x_1^2 + x_2^2 oraz wektory gradientu');
xlabel('x_1');
ylabel('x_2');
axis equal;
grid on;

% Legenda dla wektorów gradientu
legend('V(x_1, x_2)', 'Gradient ∇V(x_1, x_2)', 'Location', 'Northwest');

hold off;
