import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

# Wybór urządzenia (GPU lub CPU)
:contentReference[oaicite:1]{index=1}
:contentReference[oaicite:2]{index=2}

# Ładowanie MNIST
:contentReference[oaicite:3]{index=3}
:contentReference[oaicite:4]{index=4}
:contentReference[oaicite:5]{index=5}
:contentReference[oaicite:6]{index=6}

# Prosty model konwolucyjny (SimpleCNN)
:contentReference[oaicite:7]{index=7}
    :contentReference[oaicite:8]{index=8}
        super().__init__()
        :contentReference[oaicite:9]{index=9}
            :contentReference[oaicite:10]{index=10}
            :contentReference[oaicite:11]{index=11}
            nn.Flatten(),
            :contentReference[oaicite:12]{index=12}
            :contentReference[oaicite:13]{index=13}
        )

    def forward(self, x):
        return self.net(x)

# Klasyczny LeNet jako model ofiary
:contentReference[oaicite:14]{index=14}
    :contentReference[oaicite:15]{index=15}
        super().__init__()
        :contentReference[oaicite:16]{index=16}
            :contentReference[oaicite:17]{index=17}
            :contentReference[oaicite:18]{index=18}
            nn.Flatten(),
            :contentReference[oaicite:19]{index=19}
            :contentReference[oaicite:20]{index=20}
            :contentReference[oaicite:21]{index=21}
        )

    def forward(self, x):
        return self.net(x)

# Funkcja treningowa
:contentReference[oaicite:22]{index=22}
    model.train()
    :contentReference[oaicite:23]{index=23}
    :contentReference[oaicite:24]{index=24}
    :contentReference[oaicite:25]{index=25}
        :contentReference[oaicite:26]{index=26}
            :contentReference[oaicite:27]{index=27}
            optimizer.zero_grad()
            :contentReference[oaicite:28]{index=28}
            loss.backward()
            optimizer.step()

# Atak FGSM
:contentReference[oaicite:29]{index=29}
    :contentReference[oaicite:30]{index=30}
    :contentReference[oaicite:31]{index=31}
    :contentReference[oaicite:32]{index=32}
    model.zero_grad()
    loss.backward()
    :contentReference[oaicite:33]{index=33}

# Atak PGD
:contentReference[oaicite:34]{index=34}
    :contentReference[oaicite:35]{index=35}
    :contentReference[oaicite:36]{index=36}
    :contentReference[oaicite:37]{index=37}
        :contentReference[oaicite:38]{index=38}
        :contentReference[oaicite:39]{index=39}
        model.zero_grad()
        loss.backward()
        :contentReference[oaicite:40]{index=40}
        :contentReference[oaicite:41]{index=41}
        :contentReference[oaicite:42]{index=42}
    return adv

# Funkcja ataku + obliczenia SSIM
:contentReference[oaicite:43]{index=43}
    model_attacker.eval()
    model_victim.eval()

    images, labels = next(iter(loader))
    images, labels = images.to(device), labels.to(device)

    adv_fgsm = fgsm_attack(model_attacker, images, labels, epsilon)
    adv_pgd  = pgd_attack(model_attacker, images, labels, epsilon)

    with torch.no_grad():
        out_f = model_victim(adv_fgsm)
        out_p = model_victim(adv_pgd)
        acc_f = (out_f.argmax(1) == labels).float().mean().item() * 100
        acc_p = (out_p.argmax(1) == labels).float().mean().item() * 100

    # Detach + CPU + NumPy, by móc obliczyć SSIM bez błędów gradientów :contentReference[oaicite:44]{index=44}
    orig_np = images.detach().cpu().numpy()
    advf_np = adv_fgsm.detach().cpu().numpy()
    advp_np = adv_pgd.detach().cpu().numpy()

    ssim_f = [ssim(orig_np[i].squeeze(), advf_np[i].squeeze(), data_range=1.0) for i in range(min(100, orig_np.shape[0]))]
    ssim_p = [ssim(orig_np[i].squeeze(), advp_np[i].squeeze(), data_range=1.0) for i in range(min(100, orig_np.shape[0]))]

    mean_ssim_f = np.mean(ssim_f)
    mean_ssim_p = np.mean(ssim_p)

    print(f"Epsilon={epsilon:.2f} | FGSM acc={acc_f:.2f}%, SSIM={mean_ssim_f:.3f} | " +
          f"PGD acc={acc_p:.2f}%, SSIM={mean_ssim_p:.3f}")

    if show_examples:
        plt.figure(figsize=(10, 4))
        for i in range(6):
            plt.subplot(2, 6, i + 1)
            plt.imshow(adv_fgsm[i].cpu().squeeze(), cmap="gray")
            plt.title(f"FGSM: {out_f.argmax(1)[i].item()}")
            plt.axis("off")
            plt.subplot(2, 6, i + 7)
            plt.imshow(adv_pgd[i].cpu().squeeze(), cmap="gray")
            plt.title(f"PGD: {out_p.argmax(1)[i].item()}")
            plt.axis("off")
        plt.suptitle(f"Adversarial examples (ε={epsilon})")
        plt.tight_layout()
        plt.show()

# Inicjalizacja i trening
:contentReference[oaicite:45]{index=45}
:contentReference[oaicite:46]{index=46}

:contentReference[oaicite:47]{index=47}
:contentReference[oaicite:48]{index=48}
:contentReference[oaicite:49]{index=49}
:contentReference[oaicite:50]{index=50}

# Ocena modelu ofiary na czystych danych
:contentReference[oaicite:51]{index=51}
    model.eval()
    :contentReference[oaicite:52]{index=52}
    :contentReference[oaicite:53]{index=53}
        :contentReference[oaicite:54]{index=54}
            :contentReference[oaicite:55]{index=55}
            :contentReference[oaicite:56]{index=56}
            :contentReference[oaicite:57]{index=57}
            :contentReference[oaicite:58]{index=58}
    :contentReference[oaicite:59]{index=59}

:contentReference[oaicite:60]{index=60}

# Przeprowadzenie ataków
:contentReference[oaicite:61]{index=61}
:contentReference[oaicite:62]{index=62}
    :contentReference[oaicite:63]{index=63}
