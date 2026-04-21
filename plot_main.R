#
# ! -------------------------------------------------- Leitura de Documentos --------------------------------------------------
caminho <- "data/dados.txt"
df <- read.csv(caminho, comment.char = "#", header = FALSE)
colnames(df) <- c("v", "fv")
caminho_car <- "data/dados_car.txt"
v_car <- read.csv(caminho_car, comment.char = "#", header = FALSE)
colnames(v_car) <- c("v", "fv")
v_mp <- v_car[1, 1]
v_med <- v_car[2, 1]
v_rms <- v_car[3, 1]
# ! -------------------------------------------------- Determinação de Limites --------------------------------------------------
y_max_limit <- max(df$fv) * 1.10
x_max_limit <- v_med * 3
# ! -------------------------------------------------- Inicializa e Configura Dispositivo Gráfico --------------------------------------------------
png("figures/maxwell_boltzmann_plot.png", width = 8, height = 6, units = "in", res = 300)
par(mar = c(5, 5, 4, 2) + 0.1, mgp = c(3, 0.7, 0), las = 1)
# ! -------------------------------------------------- Inicia Criação de Gráficas --------------------------------------------------
plot(df$v, df$fv,
  type = "l", lwd = 3, col = "black",
  xlab = expression(paste("Velocity, ", italic(v), " (m/s)")),
  ylab = expression(paste("Probability Density, ", italic(f(v)), " (s/m)")),
  main = "Maxwell-Boltzmann Velocity Distribution",
  xlim = c(0, x_max_limit),
  ylim = c(0, y_max_limit),
  bty = "l", cex.lab = 1.2, cex.main = 1.3
)
abline(v = v_mp, col = "#D55E00", lwd = 2, lty = 2)
abline(v = v_med, col = "#0072B2", lwd = 2, lty = 2)
abline(v = v_rms, col = "#009E73", lwd = 2, lty = 2)
legend("topright",
  legend = c(
    bquote(italic(v)[mp] == .(round(v_mp, 2))),
    bquote(italic(v)[mean] == .(round(v_med, 2))),
    bquote(italic(v)[rms] == .(round(v_rms, 2)))
  ),
  col = c("#D55E00", "#0072B2", "#009E73"),
  lty = 2, lwd = 2, bty = "n", cex = 1.1
)
dev.off()
cat("O gráfico foi gerado com sucesso!\n")
