"""Markdown parser module for py_dirbuilder."""

from typing import List, Tuple
from py_dirbuilder.models import Node
from py_dirbuilder.parser.base import BaseParser


class MarkdownParser(BaseParser):
    """Parser for Markdown-formatted directory structures."""
    
    def parse(self, source: str) -> Node:
        """Parse Markdown list into a tree structure.
        
        Args:
            source: Markdown-formatted string with directory structure.
            
        Returns:
            Root node of the parsed tree.
        """
        lines = source.strip().split('\n')
        if not lines:
            return Node(name='root', is_file=False)
        
        # Detect format type
        has_tree_chars = any('├' in line or '└' in line or '│' in line for line in lines)
        has_bullets = any(line.lstrip().startswith(('-', '*')) for line in lines)
        
        if has_tree_chars:
            return self._parse_tree_format(lines)
        elif has_bullets:
            return self._parse_markdown_format(lines)
        else:
            # Try to parse as simple list without bullets
            return self._parse_simple_format(lines)
    
    def _parse_tree_format(self, lines: List[str]) -> Node:
        """Parse tree-style format."""
        # First line is usually the root
        first_line = lines[0].strip()
        if first_line and not any(c in first_line for c in ('├', '└', '│')):
            root = Node(name=first_line.rstrip('/'), is_file=False)
            start_idx = 1
        else:
            root = Node(name='root', is_file=False)
            start_idx = 0
        
        stack: List[Tuple[Node, int]] = [(root, -1)]
        
        for line in lines[start_idx:]:
            if not line.strip():
                continue
            
            # Calculate depth by counting │ characters
            depth = 0
            i = 0
            while i < len(line):
                if i + 4 <= len(line) and line[i:i+4] == '│   ':
                    depth += 1
                    i += 4
                elif line[i] == ' ':
                    i += 1
                else:
                    break
            
            # Extract content after tree symbols
            remaining = line[i:]
            if remaining.startswith('├── ') or remaining.startswith('└── '):
                content = remaining[4:]
            elif remaining.startswith('├─ ') or remaining.startswith('└─ '):
                content = remaining[3:]
            else:
                content = remaining
            
            content = content.strip()
            
            # Remove comments
            if '#' in content:
                content = content.split('#', 1)[0].strip()
            
            if not content:
                continue
            
            # Determine file or directory
            is_file = '.' in content and not content.endswith('/')
            name = content.rstrip('/')
            node = Node(name=name, is_file=is_file)
            
            # Find correct parent based on depth
            while len(stack) > depth + 1:
                stack.pop()
            
            if stack:
                parent = stack[-1][0]
                parent.children.append(node)
            
            # Always update stack for both files and directories
            stack.append((node, depth))
        
        return root
    
    def _parse_markdown_format(self, lines: List[str]) -> Node:
        """Parse markdown bullet list format."""
        # Check if first line is root without bullet
        first_line = lines[0].strip()
        if first_line and not first_line.startswith(('-', '*')):
            root = Node(name=first_line.rstrip('/'), is_file=False)
            start_idx = 1
        else:
            root = Node(name='root', is_file=False)
            start_idx = 0
        
        stack: List[Tuple[Node, int]] = [(root, -1)]
        
        for line in lines[start_idx:]:
            if not line.strip():
                continue
            
            indent = len(line) - len(line.lstrip())
            content = line.lstrip()
            
            if content.startswith(('-', '*')):
                content = content[1:].strip()
            else:
                continue
            
            if '#' in content:
                content = content.split('#', 1)[0].strip()
            
            if not content:
                continue
            
            is_file = '.' in content and not content.endswith('/')
            name = content.rstrip('/')
            node = Node(name=name, is_file=is_file)
            
            while len(stack) > 1 and stack[-1][1] >= indent:
                stack.pop()
            
            parent = stack[-1][0]
            parent.children.append(node)
            stack.append((node, indent))
        
        return root
    
    def _parse_simple_format(self, lines: List[str]) -> Node:
        """Parse simple indented format without bullets."""
        root = Node(name='root', is_file=False)
        stack: List[Tuple[Node, int]] = [(root, -1)]
        
        for line in lines:
            if not line.strip():
                continue
            
            indent = len(line) - len(line.lstrip())
            content = line.strip()
            
            if '#' in content:
                content = content.split('#', 1)[0].strip()
            
            if not content:
                continue
            
            is_file = '.' in content and not content.endswith('/')
            name = content.rstrip('/')
            node = Node(name=name, is_file=is_file)
            
            while len(stack) > 1 and stack[-1][1] >= indent:
                stack.pop()
            
            parent = stack[-1][0]
            parent.children.append(node)
            stack.append((node, indent))
        
        return root