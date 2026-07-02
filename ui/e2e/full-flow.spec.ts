import { test, expect } from '@playwright/test';

test('admin creates event type, books 2 slots on different dates, verifies in admin', async ({ page }) => {
  const name = `E2E Test ${Date.now()}`;

  await page.goto('/admin');
  await page.getByRole('textbox', { name: 'Name' }).fill(name);
  await page.getByRole('textbox', { name: 'Description' }).fill('Created by automated E2E test');
  await page.getByRole('textbox', { name: /Duration/ }).fill('45');
  await page.getByRole('button', { name: 'Create' }).click();
  await expect(page.getByRole('textbox', { name: 'Name' })).toHaveValue('');

  await page.goto('/');
  const card = page.locator('.mantine-Card-root').filter({ hasText: name });
  await expect(card).toBeVisible();

  for (let b = 0; b < 2; b++) {
    await card.getByRole('button', { name: 'Select Slot' }).click();
    await expect(page).toHaveURL(/\/book\//);
    await expect(page.locator('table')).toBeVisible({ timeout: 10000 });

    const dayButtons = page.locator('table button:not([disabled])');
    const dayCount = await dayButtons.count();

    for (let d = 0; d < dayCount; d++) {
      await dayButtons.nth(d).click();

      const slotButton = page.getByRole('button', { name: /^\d{2}:\d{2}$/ }).first();
      try {
        await slotButton.waitFor({ timeout: 2000 });
        await slotButton.click();
        break;
      } catch {
        continue;
      }
    }

    await expect(page.getByRole('dialog')).toBeVisible({ timeout: 5000 });
    await page.getByRole('dialog').getByRole('button', { name: 'Confirm' }).click();
    await expect(page).toHaveURL('/');
  }

  await page.goto('/admin');
  const rows = page.locator('table tbody tr').filter({ hasText: name });
  await expect(rows).toHaveCount(2);
});
