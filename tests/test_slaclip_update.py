import math

import torch

from opacus.optimizers.slaclipoptimizer import SlaClipOptimizer


def test_slaclip_update_equation():
    model = torch.nn.Linear(1, 1)
    opt = torch.optim.SGD(model.parameters(), lr=0.1)
    dp = SlaClipOptimizer(
        opt,
        noise_multiplier=1.0,
        max_grad_norm=2.0,
        expected_batch_size=1,
        num_slots=2,
        eta=0.5,
        beta=0.5,
        gamma=0.5,
        strict_paper_check=True,
    )
    s_hat = torch.tensor([0.2, 0.4])
    C_t = 2.0
    gamma_t = max(0.0, min(1.0, 1.0 - 0.5 * (1.0 - (0.4 / 2.0))))
    expected = C_t * math.exp(0.5 * (gamma_t - 0.2))
    actual = dp._update_threshold(C_t, s_hat)
    assert abs(actual - expected) < 1e-9
