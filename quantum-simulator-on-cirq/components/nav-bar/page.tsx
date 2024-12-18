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
    <Nav>
      <ProjectName>Marvelous Quantum</ProjectName>
      <NavLinks>
        <NavItem href="/" isactive={pathname === '/'}>Home</NavItem>
        <NavItem href="/circuits" isactive={pathname === '/circuits'}>Circuits</NavItem>
        <NavItem href="/circuitskeys" isactive={pathname === '/circuitskeys'}>Circuits keys</NavItem>
        <NavItem href="/gates" isactive={pathname === '/gates'}>Gates</NavItem>
        <NavItem href="/blochSphere" isactive={pathname === '/blochSphere'}>BlochSphere</NavItem>
      </NavLinks>
    </Nav>
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

const NavItem = styled(Link)<NavLinkProps>`
  color: #000;
  text-decoration: none;
  font-size: 1.2em;
  font-weight: bold;
  border-bottom: ${({ isactive }) => (isactive ? '2px solid #000' : '2px solid transparent')};
  padding-bottom: 5px;
  transition: border-bottom 0.3s;

  &:hover {
    border-bottom: 2px solid #000;
  }
`;

export default Navbar;
