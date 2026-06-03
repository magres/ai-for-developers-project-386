import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import { AppShell, Group, Title, Switch, Text } from '@mantine/core';

export default function Layout() {
  const navigate = useNavigate();
  const location = useLocation();
  const isAdmin = location.pathname.startsWith('/admin');

  const toggle = () => {
    navigate(isAdmin ? '/' : '/admin');
  };

  return (
    <AppShell header={{ height: 60 }} padding="md">
      <AppShell.Header>
        <Group h="100%" px="md" justify="space-between">
          <Title order={3} onClick={() => navigate('/')} style={{ cursor: 'pointer' }}>
            Calendar Booking
          </Title>
          <Group>
            <Text size="sm" c={!isAdmin ? 'blue' : 'dimmed'} fw={!isAdmin ? 600 : 400}>Guest</Text>
            <Switch checked={isAdmin} onChange={toggle} />
            <Text size="sm" c={isAdmin ? 'blue' : 'dimmed'} fw={isAdmin ? 600 : 400}>Admin</Text>
          </Group>
        </Group>
      </AppShell.Header>
      <AppShell.Main>
        <Outlet />
      </AppShell.Main>
    </AppShell>
  );
}
