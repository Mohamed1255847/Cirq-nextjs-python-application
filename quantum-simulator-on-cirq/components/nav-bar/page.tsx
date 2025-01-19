'use client';
import Link from 'next/link';
import styled from 'styled-components';
import { usePathname } from 'next/navigation';
import { FC } from 'react';

interface NavLinkProps {
  href: string;
  isactive?: boolean;
}

const Navbar: FC = () => {
  const pathname = usePathname();

  return (
    <>
      <Nav>
        <ProjectName>Marvelous Quantum</ProjectName>
        <NavLinks>
          <NavItem href="/" isactive={pathname === '/'}>Home</NavItem>
          <NavItem href="/circuits" isactive={pathname === '/circuits'}>Circuits</NavItem>
          <NavItem href="/circuitskeys" isactive={pathname === '/circuitskeys'}>Circuits keys</NavItem>
          <NavItem href="/gates" isactive={pathname === '/gates'}>Gates</NavItem>
          <NavItem href="/blochSphere" isactive={pathname === '/blochSphere'}>
            BlochSphere
          </NavItem>
          <NavItem href="/qfm" isactive={pathname === '/qfm'}>
            QFM
          </NavItem>
        </NavLinks>
      </Nav>
      {pathname === '/blochSphere' && <UnderDevelopmentLabel>Under Development</UnderDevelopmentLabel>}
    </>
  );
};

const Nav = styled.nav`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #fff;
  z-index: 1000;
`;

const ProjectName = styled.div`
  font-size: 1.5em;
  font-weight: bold;
  color: #000;
`;

const NavLinks = styled.div`
  display: flex;
  gap: 20px;
`;

const NavItem = styled(Link) <NavLinkProps>`
  color: #000;
  text-decoration: none;
  font-size: 1.2em;
  font-weight: bold;
  border-bottom: ${({ isactive }) => (isactive ? '2px solid #000' : '2px solid transparent')};
  padding-bottom: 5px;
  transition: border-bottom 0.3s;
  display: flex;
  align-items: center;
  gap: 8px;

  &:hover {
    border-bottom: 2px solid #000;
  }
`;

const UnderDevelopmentLabel = styled.div`
  width: 100%;
  height: 60px;
  background-color: #0d44da;
  color: #ffffff;
  font-size: 3em;
  padding: 2px 6px;
  border-radius: 4px;
  text-align: center;
`;

export default Navbar;