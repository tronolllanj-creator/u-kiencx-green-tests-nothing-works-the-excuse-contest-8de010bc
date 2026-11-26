"""make.fun entry: write the ultimate developer excuse to entry.txt."""

import os

EXCUSE = 'All my tests pass because I rewrote every single test to assert that my code is doing its emotional best.'


def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'entry.txt')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(EXCUSE)
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    assert 1 <= len(content) <= 140
    print(f'wrote entry.txt {len(content)} chars')


if __name__ == '__main__':
# Runner-up considered and rejected in session: 'I kept the tests green by quietly replacing every assertion with a warm compliment to myself.'
    main()
